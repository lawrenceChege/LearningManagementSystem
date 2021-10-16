from django.contrib import admin

from api.models import CourseManager, CourseEnrollment, SubjectTeacher, SubjectEnrollment, UnitTeacher, UnitEnrollment, \
	QuizEnrollment, StudentQuizAnswer, QuizResult, AssignmentEnrollment, StudentAssignmentAnswer, AssignmentResult


@admin.register(CourseManager)
class CourseManagerAdmin(admin.ModelAdmin):
    """
    Admin for CourseManager model
    """
    list_filter = ('date_created', 'course', 'manager',)
    list_display = ('course', 'manager', 'state', 'date_created', 'date_modified')
    search_fields = ('course__name', 'manager__username', 'state__name',
                     'course__code', 'manager__phone_number')


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    """
    Admin for CourseEnrollment model
    """
    list_filter = ('date_created', 'course', 'student',)
    list_display = ('course', 'student', 'is_completed', 'level', 'amount_paid', 'receipt',
                    'state', 'date_created', 'date_modified')
    search_fields = ('course__name', 'student__username', 'state__name', 'receipt',
                     'course__code', 'student__phone_number')


@admin.register(SubjectTeacher)
class SubjectTeacherAdmin(admin.ModelAdmin):
    """
    Admin for SubjectTeacher model
    """
    list_filter = ('date_created', 'subject', 'teacher')
    list_display = ('subject', 'teacher', 'is_part_time', 'state', 'date_created', 'date_modified')
    search_fields = ('subject__name', 'teacher__username', 'state__name', 'receipt',
                     'subject__code', 'teacher__phone_number')


@admin.register(SubjectEnrollment)
class SubjectEnrollmentAdmin(admin.ModelAdmin):
    """
    Admin for SubjectEnrollment model
    """
    list_filter = ('date_created', 'subject', 'student',)
    list_display = ('subject', 'student', 'is_completed', 'level',  'state', 'date_created', 'date_modified')
    search_fields = ('subject__name', 'student__username', 'state__name', 'subject__code', 'student__phone_number')


@admin.register(UnitTeacher)
class UnitTeacherAdmin(admin.ModelAdmin):
    """
    Admin for UnitTeacher model
    """
    list_filter = ('date_created', 'unit', 'teacher')
    list_display = ('unit', 'teacher', 'is_part_time', 'state', 'date_created', 'date_modified')
    search_fields = ('unit__name', 'teacher__username', 'state__name', 'unit__code', 'teacher__phone_number')


@admin.register(UnitEnrollment)
class UnitEnrollmentAdmin(admin.ModelAdmin):
    """
    Admin for UnitEnrollment model
    """
    list_filter = ('date_created', 'unit', 'student',)
    list_display = ('unit', 'student', 'is_completed', 'level',  'state', 'date_created', 'date_modified')
    search_fields = ('unit__name', 'student__username', 'state__name', 'unit__code', 'student__phone_number')


@admin.register(QuizEnrollment)
class QuizEnrollmentAdmin(admin.ModelAdmin):
    """
    Admin for QuizEnrollment model
    """
    list_filter = ('date_created', 'quiz', 'student',)
    list_display = ('quiz', 'student', 'is_completed', 'level',  'state', 'date_created', 'date_modified')
    search_fields = ('quiz__name', 'student__username', 'state__name', 'quiz__code', 'student__phone_number')


@admin.register(StudentQuizAnswer)
class StudentQuizAnswerAdmin(admin.ModelAdmin):
    """
    Admin for StudentQuizAnswer model
    """
    list_filter = ('date_created', 'enrolled_student__quiz', 'enrolled_student__student',)
    list_display = ('enrolled_student', 'quiz_question', 'answer',  'state', 'date_created', 'date_modified')
    search_fields = ('enrolled_student__quiz__name', 'enrolled_student__student__username', 'state__name',
                     'enrolled_student__quiz__code', 'enrolled_student__student__phone_number')


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    """
    Admin for QuizResult model
    """
    list_filter = ('date_created', 'quiz', 'enrolled_student__student',)
    list_display = ('enrolled_student', 'quiz', 'marks', 'grade', 'state', 'date_created', 'date_modified')
    search_fields = ('quiz__name', 'enrolled_student__student__username', 'state__name',
                     'quiz__code', 'enrolled_student__student__phone_number')


@admin.register(AssignmentEnrollment)
class AssignmentEnrollmentAdmin(admin.ModelAdmin):
    """
    Admin for AssignmentEnrollment model
    """
    list_filter = ('date_created', 'assignment', 'student',)
    list_display = ('assignment', 'student', 'is_completed', 'level',  'state', 'date_created', 'date_modified')
    search_fields = ('assignment__name', 'student__username', 'state__name', 'assignment__code', 'student__phone_number')


@admin.register(StudentAssignmentAnswer)
class StudentAssignmentAnswerAdmin(admin.ModelAdmin):
    """
    Admin for StudentAssignmentAnswer model
    """
    list_filter = ('date_created', 'enrolled_student__assignment', 'enrolled_student__student',)
    list_display = ('enrolled_student', 'assignment_question', 'answer',  'state', 'date_created', 'date_modified')
    search_fields = ('enrolled_student__assignment__name', 'enrolled_student__student__username', 'state__name',
                     'enrolled_student__assignment__code', 'enrolled_student__student__phone_number')


@admin.register(AssignmentResult)
class AssignmentResultAdmin(admin.ModelAdmin):
    """
    Admin for AssignmentResult model
    """
    list_filter = ('date_created', 'assignment', 'enrolled_student__student',)
    list_display = ('enrolled_student', 'assignment', 'marks', 'grade', 'state', 'date_created', 'date_modified')
    search_fields = ('assignment__name', 'enrolled_student__student__username', 'state__name',
                     'assignment__code', 'enrolled_student__student__phone_number')

