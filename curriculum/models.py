from django.db import models

from base.models import GenericBaseModel, DurationType, Currency, BaseModel, State
from users.models import User


class BaseCourse(GenericBaseModel):
    """
    Base definition of courses, subjects and units
    """
    code = models.CharField(max_length=6, default='100000')
    duration_type = models.ForeignKey(DurationType, on_delete=models.CASCADE)
    duration = models.IntegerField(max_length=10)
    outline = models.TextField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(max_length=10, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)
    open_to_teacher = models.BooleanField(default=False)
    open_to_students = models.BooleanField(default=False)

    class Meta(object):
        abstract = True


class Course(BaseCourse):
    """
    The model for holding subjects eg Computer Science
    """
    subjects = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Courses"


class Subject(BaseCourse):
    """
    The model for holding subjects eg Data Structures
    """
    units = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Subjects"


class CourseSubject(BaseModel):
    """
    The model for holding CourseSubject
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.course.name, self.subject.name)

    class Meta(object):
        verbose_name_plural = "Course Subjects"


class Unit(BaseCourse):
    """
    The model for holding units
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapters = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Units"


class CourseUnit(BaseModel):
    """
    The model for holding CourseUnit
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit = models.ForeignKey(Subject, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.course.name, self.unit.name)

    class Meta(object):
        verbose_name_plural = "Course Units"


class Chapter(BaseCourse):
    """
    The model for holding chapters
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    chapter_no = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.unit.name)

    class Meta(object):
        verbose_name_plural = "Chapters"


class ChapterNotes(GenericBaseModel):
    """
    The model for holding notes
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.slug)

    class Meta(object):
        verbose_name_plural = "Notes"


class ChapterVideo(GenericBaseModel):
    """
    The model for holding video
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader')
    video = models.FileField()

    def __str__(self):
        return '%s %s' % (self.name, self.slug)

    class Meta(object):
        verbose_name_plural = "Notes"


class Quiz(GenericBaseModel):
    """
    The model for holding quizzes
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    pass_mark = models.IntegerField(max_length=3, default=0)
    total_marks = models.IntegerField(max_length=3, default=100)
    open_to_teacher = models.BooleanField(default=False)
    open_to_students = models.BooleanField(default=False)
    questions = models.IntegerField(max_length=3, default=10)

    def __str__(self):
        return '%s %s' % (self.name, self.pass_mark)

    class Meta(object):
        verbose_name_plural = "Quizzes"


class QuizQuestion(BaseModel):
    """
    The model for holding Quiz Question
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField()
    question_no = models.IntegerField(max_length=3, default=0)
    marks = models.IntegerField(max_length=3, default=0)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.question_no, self.question)

    class Meta(object):
        verbose_name_plural = "Quiz Question"


class QuizQuestionChoice(BaseModel):
    """
    The model for holding quiz question choices
    """
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    choice = models.TextField()
    is_answer = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.quiz_question.question_no, self.choice)

    class Meta(object):
        verbose_name_plural = "Quiz Question Choice"


class Assignment(GenericBaseModel):
    """
    The model for holding homework
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateTimeField()
    questions = models.IntegerField(max_length=3, default=10)

    def __str__(self):
        return '%s %s' % (self.name, self.due_date)

    class Meta(object):
        verbose_name_plural = "Assignments"


class AssignmentQuestion(GenericBaseModel):
    """
    The model for holding homework
    """
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField()
    marks = models.IntegerField(max_length=3, default=0)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Assignment Questions"
