import uuid
from django.utils import timezone
from django.db import models


class State(GenericBaseModel):
    """
    States for objects lifecycle e.g. "Active", "Activation Pending", "Reversed", etc
    """
    name = models.CharField(max_length=35, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    def __str__(self):
        return '%s' % self.name

    class Meta(object):
        ordering = ('name',)
        unique_together = ('name',)

    @classmethod
    def default_state(cls):
        """
    The default Active state. Help in ensuring that the admin will be created without supplying the state at the
    command like.
    @return: The active state, if it exists, or create a new one if it doesn't exist.
    @rtype: str | None
    """
        # noinspection PyBroadException

        state = cls.objects.get(name='Active')
        return state.id

    @classmethod
    def disabled_state(cls):
        """
        The default Disabled state. Help in ensuring that the admin will be created without supplying the state at the
        command like.
        @return: The active state, if it exists, or create a new one if it doesn't exist.
        @rtype: str | None
        """
        # noinspection PyBroadException

        state = cls.objects.get(name='Disabled')
        return state


class BaseModel(models.Model):
    """
    Define repetitive methods to enhance re-usability.
    """
    id = models.UUIDField(max_length=50, default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    date_modified = models.DateTimeField(auto_now=True)  # (default = timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)  # (default = timezone.now)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta(object):
        abstract = True

class GenericBaseModel(BaseModel):
    """
    Define repetitive methods to avoid cycles of redefining in every model.
    """
    name = models.CharField(max_length=35, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)

    class Meta(object):
        abstract = True

class Grade(GenericBaseModel):
    """
    Define repetitive methods to avoid cycles of redefining in every model.
    """
    code = models.CharField(max_length=5)
    marks_lower = models.IntegerField(max_length=3)
    marks_upper = models.IntegerField(max_length=3)

    class Meta(object):
        abstract = True

class DurationType(GenericBaseModel):
    """
    Defines the duration of a loan e.g. Monthly, Weekly, Quarterly
    """

    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta(GenericBaseModel.Meta):
        unique_together = ('name', 'state')

class Currency(GenericBaseModel):
    """
    Defines a type of Currency and its code e.g US Dollar - USD
    """

    state = models.ForeignKey(State, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta(GenericBaseModel.Meta):
        verbose_name_plural = 'Currencies'
        unique_together = ('name',)
