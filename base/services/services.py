from base.models import State, Grade, DurationType, Currency
from base.services.servicebase import ServiceBase


class StateService(ServiceBase):
	"""
		The service for handling CRUD events for the State model
	"""
	manager = State.objects


class GradeService(ServiceBase):
	"""
		The service for handling CRUD events for the Grade model
	"""
	manager = Grade.objects


class DurationTypeService(ServiceBase):
	"""
		The service for handling CRUD events for DurationType model
	"""
	manager = DurationType.objects


class CurrencyService(ServiceBase):
	"""
		The service for handling CRUD events for Currency model
	"""
	manager = Currency.objects