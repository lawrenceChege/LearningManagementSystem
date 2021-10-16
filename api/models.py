from django.db import models

from base.models import GenericBaseModel, BaseModel, State, Grade
from curriculum.models import Course, Subject, Unit, Quiz, QuizQuestion, QuizQuestionChoice, Assignment, \
    AssignmentQuestion
from users.models import User


class BaseEnrollment(BaseModel):
    """
    Base Definition for enrollments
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    level = models.IntegerField(max_length=2, default=0)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta(object):
        abstract = True


class BaseTeacher(BaseModel):
    """
    Base Definition for teacher assignment
    """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    is_part_time = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta(object):
        abstract = True


class CourseManager(BaseModel):
    """
    The model for teacher in charge of a course
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.course.name, self.manager.username)

    class Meta(object):
        verbose_name_plural = "Course Manager"


class CourseEnrollment(BaseEnrollment):
    """
    The model for students registering for a course
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount_paid = models.IntegerField(max_length=10, default=0)
    receipt = models.CharField(max_length=20, default='100000')

    def __str__(self):
        return '%s %s' % (self.course.name, self.student.username)

    class Meta(object):
        verbose_name_plural = "Course enrollment"


class SubjectTeacher(BaseTeacher):
    """
    The model for teacher in charge of a subject
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.subject.name, self.teacher.username)

    class Meta(object):
        verbose_name_plural = "Subject Teacher"


class SubjectEnrollment(BaseEnrollment):
    """
    The model for students currently taking a subject
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.subject.name, self.student.username)

    class Meta(object):
        verbose_name_plural = "Subject Enrollment"


class UnitTeacher(BaseTeacher):
    """
    The model for teacher in charge of a unit
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.unit.name, self.teacher.username)

    class Meta(object):
        verbose_name_plural = "Unit Teacher"


class UnitEnrollment(BaseEnrollment):
    """
    The model for students currently taking a unit
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.unit.name, self.student.username)

    class Meta(object):
        verbose_name_plural = "Unit Enrollment"


class QuizEnrollment(BaseEnrollment):
    """
    The model for students currently taking a unit
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.quiz.name, self.student.username)

    class Meta(object):
        verbose_name_plural = "Quiz Enrollment"


class StudentQuizAnswer(BaseModel):
    """
    The model for holding results for quizzes
    """
    enrolled_student = models.ForeignKey(QuizEnrollment, on_delete=models.CASCADE)
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    quiz_question_choice = models.ForeignKey(QuizQuestionChoice, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.quiz_question.question, self.quiz_question_choice.choice)

    class Meta(object):
        verbose_name_plural = "Quiz Answers"


class QuizResult(BaseModel):
    """
    The model for holding results for quizzes
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    enrolled_student = models.ForeignKey(QuizEnrollment, on_delete=models.CASCADE)
    marks = models.IntegerField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.quiz.name, self.marks)

    class Meta(object):
        verbose_name_plural = "Quiz Results"


class AssignmentEnrollment(BaseEnrollment):
    """
    The model for students currently taking an Assignment
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.assignment.name, self.student.username)

    class Meta(object):
        verbose_name_plural = "Assignment Enrollment"


class StudentAssignmentAnswer(BaseModel):
    """
    The model for holding results for Assignment answers
    """
    enrolled_student = models.ForeignKey(AssignmentEnrollment, on_delete=models.CASCADE)
    assignment_question = models.ForeignKey(AssignmentQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    marks = models.IntegerField(max_length=3, default=0)
    marked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.assignment_question.question, self.answer)

    class Meta(object):
        verbose_name_plural = "Assignment Answers"


class AssignmentResult(BaseModel):
    """
    The model for holding results for quizzes
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    enrolled_student = models.ForeignKey(AssignmentEnrollment, on_delete=models.CASCADE)
    marks = models.IntegerField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.assignmentname, self.marks)

    class Meta(object):
        verbose_name_plural = "Assignment Results"
