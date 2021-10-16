from django.contrib import admin

from curriculum.models import Course, Subject, CourseSubject, Unit, CourseUnit, Chapter, ChapterNotes, ChapterVideo, \
	Quiz, QuizQuestion, QuizQuestionChoice, Assignment, AssignmentQuestion


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	"""
	Admin for Course model
	"""
	list_filter = ('date_created',)
	list_display = (
		'name', 'description', 'code', 'duration_type', 'duration', 'outline', 'currency',
		'amount', 'poster', 'open_to_teacher', 'open_to_students', 'subjects',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'code', 'state__name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	"""
	Admin for Subject model
	"""
	list_filter = ('date_created',)
	list_display = (
		'name', 'description', 'code', 'duration_type', 'duration', 'outline', 'currency',
		'amount', 'poster', 'open_to_teacher', 'open_to_students', 'units',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'code', 'state__name')


@admin.register(CourseSubject)
class CourseSubjectAdmin(admin.ModelAdmin):
	"""
	Admin for CourseSubject model
	"""
	list_filter = ('date_created', 'course')
	list_display = ('course', 'subject', 'state', 'date_created', 'date_modified')
	search_fields = ('course__name', 'course__code', 'subject__name', 'subject__code', 'state__name')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
	"""
	Admin for Unit model
	"""
	list_filter = ('date_created', 'subject')
	list_display = (
		'subject', 'name', 'description', 'code', 'duration_type', 'duration', 'outline', 'currency',
		'amount', 'poster', 'open_to_teacher', 'open_to_students', 'chapters',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'code', 'state__name')


@admin.register(CourseUnit)
class CourseUnitAdmin(admin.ModelAdmin):
	"""
	Admin for CourseUnit model
	"""
	list_filter = ('date_created', 'course')
	list_display = ('course', 'unit', 'state', 'date_created', 'date_modified')
	search_fields = ('course__name', 'course__code', 'unit__name', 'unit__code', 'state__name')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
	"""
	Admin for Chapter model
	"""
	list_filter = ('date_created', 'unit')
	list_display = (
		'unit', 'name', 'description', 'code', 'duration_type', 'duration', 'outline', 'currency',
		'amount', 'poster', 'open_to_teacher', 'open_to_students', 'chapter_no',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'code', 'state__name')


@admin.register(ChapterNotes)
class ChapterNotesAdmin(admin.ModelAdmin):
	"""
	Admin for ChapterNotes model
	"""
	list_filter = ('date_created', 'chapter')
	list_display = (
		'chapter', 'name', 'description', 'slug', 'author', 'content',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'chapter__name', 'chapter__code', 'state__name')


@admin.register(ChapterVideo)
class ChapterVideoAdmin(admin.ModelAdmin):
	"""
	Admin for ChapterVideo model
	"""
	list_filter = ('date_created', 'chapter')
	list_display = (
		'chapter', 'name', 'description', 'slug', 'uploader', 'video',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'chapter__name', 'chapter__code', 'state__name')


@admin.register(ChapterVideo)
class ChapterVideoAdmin(admin.ModelAdmin):
	"""
	Admin for ChapterVideo model
	"""
	list_filter = ('date_created', 'chapter')
	list_display = (
		'chapter', 'name', 'description', 'slug', 'uploader', 'video',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'chapter__name', 'chapter__code', 'state__name')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
	"""
	Admin for Quiz model
	"""
	list_filter = ('date_created', 'chapter')
	list_display = (
		'subject', 'unit', 'chapter', 'name', 'description', 'pass_mark', 'total_marks',
		'open_to_teacher', 'open_to_students', 'questions',
		'state', 'date_created', 'date_modified')
	search_fields = ('name', 'subject__name', 'subject__code', 'unit__name', 'unit__code',
	                 'chapter__name', 'chapter__code', 'state__name')


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
	"""
	Admin for QuizQuestion model
	"""
	list_filter = ('date_created', 'quiz')
	list_display = (
		'quiz', 'question', 'question_no', 'marks',
		'state', 'date_created', 'date_modified')
	search_fields = ('quiz__name', 'question', 'state__name')


@admin.register(QuizQuestionChoice)
class QuizQuestionChoiceAdmin(admin.ModelAdmin):
	"""
	Admin for QuizQuestionChoice model
	"""
	list_filter = ('date_created', 'quiz_question')
	list_display = (
		'quiz_question', 'choice', 'is_answer',
		'state', 'date_created', 'date_modified')
	search_fields = ('quiz_question__quiz__name', 'quiz_question__question', 'state__name')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
	"""
	Admin for Assignment model
	"""
	list_filter = ('date_created', 'chapter')
	list_display = (
		'subject', 'unit', 'chapter', 'name', 'description', 'due_date', 'questions',
		'state', 'date_created', 'date_modified')
	search_fields = (
		'name', 'subject__name', 'subject__code', 'unit__name', 'unit__code',
		'chapter__name', 'chapter__code', 'state__name')


@admin.register(AssignmentQuestion)
class AssignmentQuestionAdmin(admin.ModelAdmin):
	"""
	Admin for AssignmentQuestion model
	"""
	list_filter = ('date_created', 'quiz')
	list_display = (
		'assignment', 'question', 'marks',
		'state', 'date_created', 'date_modified')
	search_fields = ('assignment__name', 'question', 'state__name')
