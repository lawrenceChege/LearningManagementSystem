"""
	module for Eusers
"""

from base.models import GenericBaseModel, State, BaseModel

import unicodedata
from django.contrib import auth
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
	check_password, is_password_usable, make_password,
)
# from django.contrib.auth.models import user_get_all_permissions, _user_has_perm, _user_has_module_perms
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import salted_hmac
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import _user_get_permissions, _user_has_perm, _user_has_module_perms
from django.utils import timezone

from users.managers.managers import EUserManager


class Permission(GenericBaseModel):
	"""
		This model handles system user  permission.
	"""
	parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
	simple_name = models.TextField(max_length=255, blank=True, null=True)
	for_students = models.BooleanField(default=False)
	for_teachers = models.BooleanField(default=False)
	for_admin = models.BooleanField(default=False)
	state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % self.name

	def __repr__(self):
		return f'Permission_name = {self.name},simple_name = {self.simple_name}'

	class Meta(object):
		""" model  meta data"""
		unique_together = ('name',)


class UserPassword(BaseModel):
	"""
	This model manages the user credentials. i.e:
		user(FK),password,state(FK)
	@note: Needs to be here to be used in the base class implementation.
	"""
	euser = models.ForeignKey('EUser', related_name='user_passwords', on_delete=models.CASCADE)
	password = models.CharField(_('password'), max_length=128)
	hashed_password = models.BooleanField(_('is password hashed'), default=False, editable=False)
	state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

	class Meta(object):
		ordering = ('-date_created',)
		verbose_name = 'Password'
		verbose_name_plural = 'Passwords'

	def __str__(self):
		return self.password


# noinspection PyUnusedLocal
@receiver(post_save, sender=UserPassword)
def hash_set_password(sender, instance, created, **kwargs):
	"""
		When the object is created, hash the password.
	"""
	if created and not instance.hashed_password:
		instance.hashed_password = True
		instance.password = make_password(instance.password)
		instance.save()


class AbstractEUser(models.Model):
	"""
		The base model for the e user.
	"""
	last_login = models.DateTimeField(_('last login'), blank=True, null=True)

	is_active = True

	USERNAME_FIELD = None

	EMAIL_FIELD = None

	REQUIRED_FIELDS = []

	class Meta(object):
		abstract = True

	def get_username(self):
		"""
		Return the identifying username for this User
		"""
		return getattr(self, self.USERNAME_FIELD)

	def __init__(self, *args, **kwargs):
		super(AbstractEUser, self).__init__(*args, **kwargs)
		# Stores the raw password if set_password() is called so that it can
		# be passed to password_changed() after the model is saved.
		self._password = None

	def __str__(self):
		language_code = models.CharField(max_length=5, default='en')
		return self.get_username()

	def clean(self):
		"""Clean the username field"""
		setattr(self, self.USERNAME_FIELD, self.normalize_username(self.get_username()))

	def save(self, *args, **kwargs):
		"""Override to save the user with some magic"""
		super(AbstractEUser, self).save(*args, **kwargs)
		if self._password is not None:
			password_validation.password_changed(self._password, self)
			self._password = None

	def natural_key(self):
		"""Retrieve the username for the model"""
		return self.get_username(),

	@property
	def is_anonymous(self):
		"""
		Always return False. This is a way of comparing User objects to
		anonymous users.
		"""
		return False

	@property
	def is_authenticated(self):
		"""
		Always return True. This is a way to tell if the user has been
		authenticated in templates.
		"""
		return True

	@property
	def password(self):
		"""Returns the most recent active password for the user or None"""
		# noinspection PyBroadException
		try:
			return UserPassword.objects.filter(euser=self, state__name='Active').order_by('-date_created').first()
		except Exception as e:
			return e

	# noinspection PyBroadException
	def set_password(self, raw_password):
		"""
		Sets the password for the user by creating a new active user password entry for the user instance
		@param raw_password: The raw password we are setting.
		@type raw_password: str
		"""
		try:
			self.save()  # Save our current model
			pass_update = UserPassword.objects.create(
				euser=self, password=make_password(raw_password), state_id=State.default_state(), hashed_password
				=True)
			if pass_update is not None:
				UserPassword.objects.filter(
					~Q(pk=pass_update.pk), euser=self, state__name='Active').update(
					state=State.disabled_state())
			if pass_update is not None:
				self._password = raw_password
		except Exception as e:
			print('Exception: %s' % e)

	def check_password(self, raw_password):
		"""
		Return a boolean of whether the raw_password was correct. Handles
		hashing formats behind the scenes.
		"""

		# noinspection PyUnusedLocal,PyShadowingNames
		def setter(raw_password):
			"""Sets the new password"""
			self.set_password(raw_password)
			# Password hash upgrades shouldn't be considered password changes.
			self._password = None
			self.save()

		return check_password(raw_password, str(self.password), setter)

	def set_unusable_password(self):
		"""Set a value that will never be a valid hash"""
		self._password = make_password(None)

	def has_usable_password(self):
		"""Checks if the password is usable"""
		return is_password_usable(str(self.password))

	def get_full_name(self):
		"""Retrieve the full name for the user"""
		raise NotImplementedError('subclasses of AbstractEUser must provide a get_full_name() method')

	def get_short_name(self):
		"""Retrieve a short name for the user"""
		raise NotImplementedError('subclasses of AbstractEUser must provide a get_short_name() method.')

	def get_session_auth_hash(self):
		"""
		Return an HMAC of the password field.
		"""
		key_salt = "euser.models.AbstractEUser.get_session_auth_hash"
		return salted_hmac(key_salt, self._password).hexdigest()

	@classmethod
	def get_email_field_name(cls):
		"""Get the email field name"""
		try:
			return cls.EMAIL_FIELD
		except AttributeError:
			return 'email'

	@classmethod
	def normalize_username(cls, username):
		"""Normalize the username"""
		return unicodedata.normalize('NFKC', force_str(username))


class User(BaseModel, AbstractEUser):
	"""
	The class that manages User data for access and association with corporates.
	"""
	username = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	other_name = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(_('phone number'), max_length=20)
	email = models.CharField(max_length=50)
	security_code = models.CharField(max_length=150, null=True, blank=True)
	state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)
	is_active = models.BooleanField(_('active'), default=True, help_text='User is currently active.')
	is_student = models.BooleanField(_('student'), default=False, help_text='User can login login to the dashboard.')
	is_teacher = models.BooleanField(
		_('teacher'), default=False, help_text='User has access to everything in a course/subject')
	is_admin = models.BooleanField(_('admin'), default=False, help_text='User can set up the curriculum')
	last_activity = models.DateTimeField(_('last activity'), null=True, blank=True, editable=False)
	permissions = models.ManyToManyField(
		Permission, through='ExtendedEUserPermission', blank=True, related_name="euser_set",
		related_query_name="euser", help_text='Specific permissions for this user.')

	SYNC_MODEL = True

	EMAIL_FIELD = 'email'

	USERNAME_FIELD = 'username'

	REQUIRED_FIELDS = ['phone_number', 'email']

	objects = EUserManager()

	def __str__(self):
		return '%s %s - %s' % (self.email, self.username, self.phone_number)

	def update_last_activity(self):
		"""
			Update the last time the user was activity
		"""
		self.last_activity = timezone.now()
		self.save(update_fields=["last_activity"])

	def get_full_name(self):
		"""
			Retrieves the full name for the model
		"""
		return '%s - %s %s' % (self.username, self.first_name, self.last_name)

	def get_user_name(self):
		"""
			Retrieves the short name for the user
		"""
		return str(self.username)

	def get_all_permissions(self, obj=None):
		"""
			Get all permissions
		"""
		return _user_get_permissions(self, obj, from_name=None)

	def has_perm(self, perm, obj=None):
		"""
			Returns True if the user has the specified permission. This method
			queries all available auth backends, but returns immediately if any
			backend returns True. Thus, a user who has permission from a single
			auth backend is assumed to have permission in general. If an object is
			provided, permissions for this specific object are checked.
		"""

		# Active superusers have all permissions.
		if self.is_active and self.is_admin:
			return True

		# Otherwise we need to check the backends.
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		"""
			Returns True if the user has each of the specified permissions. If
			object is passed, it checks if the user has all required perms for this
			object.
		"""
		return all(self.has_perm(perm, obj) for perm in perm_list)

	def has_module_perms(self, app_label):
		"""
			Returns True if the user has any permissions in the given app label.
			Uses pretty much the same logic as has_perm, above.
		"""
		# Active superusers have all permissions.
		if self.is_active and self.is_admin:
			return True

		return _user_has_module_perms(self, app_label)

	class Meta(BaseModel.Meta):
		unique_together = ('id',)


class UserPermission(BaseModel):
	"""
	This model maps different system roles with assigned permissions
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
	state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.user.username, self.permission.name)

	def __repr__(self):
		return f'user_name = {self.user.username}, permission_name={self.permission.name}'

	class Meta(object):
		unique_together = ('role', 'permission')