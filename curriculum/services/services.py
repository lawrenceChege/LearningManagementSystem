from base.services.servicebase import ServiceBase
from curriculum.models import Course, Subject, CourseSubject, CourseUnit, Unit, Chapter, ChapterNotes, ChapterVideo, \
	Quiz, QuizQuestion, QuizQuestionChoice, Assignment, AssignmentQuestion


class CourseService(ServiceBase):
	"""
		The service for handling CRUD events for Course model
	"""
	manager = Course.objects


class SubjectService(ServiceBase):
	"""
		The service for handling CRUD events for Subject model
	"""
	manager = Subject.objects


class CourseSubjectService(ServiceBase):
	"""
		The service for handling CRUD events for CourseSubject model
	"""
	manager = CourseSubject.objects


class UnitService(ServiceBase):
	"""
		The service for handling CRUD events for Unit model
	"""
	manager = Unit.objects


class CourseUnitService(ServiceBase):
	"""
		The service for handling CRUD events for CourseUnit model
	"""
	manager = CourseUnit.objects


class ChapterService(ServiceBase):
	"""
		The service for handling CRUD events for Chapter model
	"""
	manager = Chapter.objects


class ChapterNotesService(ServiceBase):
	"""
		The service for handling CRUD events for ChapterNotes model
	"""
	manager = ChapterNotes.objects


class ChapterVideoService(ServiceBase):
	"""
		The service for handling CRUD events for ChapterVideo model
	"""
	manager = ChapterVideo.objects


class QuizService(ServiceBase):
	"""
		The service for handling CRUD events for Quiz model
	"""
	manager = Quiz.objects


class QuizQuestionService(ServiceBase):
	"""
		The service for handling CRUD events for QuizQuestion model
	"""
	manager = QuizQuestion.objects


class QuizQuestionChoiceService(ServiceBase):
	"""
		The service for handling CRUD events for QuizQuestionChoice model
	"""
	manager = QuizQuestionChoice.objects


class AssignmentService(ServiceBase):
	"""
		The service for handling CRUD events for Assignment model
	"""
	manager = Assignment.objects


class AssignmentQuestionService(ServiceBase):
	"""
		The service for handling CRUD events for AssignmentQuestion model
	"""
	manager = AssignmentQuestion.objects
