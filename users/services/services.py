from base.services.servicebase import ServiceBase
from users.models import Permission, UserPassword, User, UserPermission


class PermissionService(ServiceBase):
	"""
		The service for handling CRUD events for Permission model
	"""
	manager = Permission.objects


class UserPasswordService(ServiceBase):
	"""
		The service for handling CRUD events for UserPassword model
	"""
	manager = UserPassword.objects


class UserService(ServiceBase):
	"""
		The service for handling CRUD events for User model
	"""
	manager = User.objects


class UserPermissionService(ServiceBase):
	"""
		The service for handling CRUD events for UserPermission model
	"""
	manager = UserPermission.objects

