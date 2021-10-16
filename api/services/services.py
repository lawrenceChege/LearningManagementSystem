from api.models import CourseManager, CourseEnrollment, SubjectTeacher, SubjectEnrollment, UnitTeacher, UnitEnrollment, \
	QuizEnrollment, StudentQuizAnswer, QuizResult, AssignmentEnrollment, StudentAssignmentAnswer, AssignmentResult
from base.services.servicebase import ServiceBase


class CourseManagerService(ServiceBase):
	"""
		The service for handling CRUD events for CourseManager model
	"""
	manager = CourseManager.objects


class CourseEnrollmentService(ServiceBase):
	"""
		The service for handling CRUD events for CourseEnrollment model
	"""
	manager = CourseEnrollment.objects


class SubjectTeacherService(ServiceBase):
	"""
		The service for handling CRUD events for SubjectTeacher model
	"""
	manager = SubjectTeacher.objects


class SubjectEnrollmentService(ServiceBase):
	"""
		The service for handling CRUD events for SubjectEnrollment model
	"""
	manager = SubjectEnrollment.objects


class UnitTeacherService(ServiceBase):
	"""
		The service for handling CRUD events for UnitTeacher model
	"""
	manager = UnitTeacher.objects


class UnitEnrollmentService(ServiceBase):
	"""
		The service for handling CRUD events for UnitEnrollment model
	"""
	manager = UnitEnrollment.objects


class QuizEnrollmentService(ServiceBase):
	"""
		The service for handling CRUD events for QuizEnrollment model
	"""
	manager = QuizEnrollment.objects


class StudentQuizAnswerService(ServiceBase):
	"""
		The service for handling CRUD events for StudentQuizAnswer model
	"""
	manager = StudentQuizAnswer.objects


class QuizResultService(ServiceBase):
	"""
		The service for handling CRUD events for QuizResult model
	"""
	manager = QuizResult.objects


class AssignmentEnrollmentService(ServiceBase):
	"""
		The service for handling CRUD events for AssignmentEnrollment model
	"""
	manager = AssignmentEnrollment.objects


class StudentAssignmentAnswerService(ServiceBase):
	"""
		The service for handling CRUD events for StudentAssignmentAnswer model
	"""
	manager = StudentAssignmentAnswer.objects


class AssignmentResultService(ServiceBase):
	"""
		The service for handling CRUD events for AssignmentResult model
	"""
	manager = AssignmentResult.objects