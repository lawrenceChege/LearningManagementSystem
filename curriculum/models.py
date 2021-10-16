from django.db import models


class Course(GenericBaseModel):
    """
    The model for holding subjects eg Maths, Eng
    """
    code = models.CharField(max_length=6, default='100000')
    duration_type = models.ForeignKey(DurationType, on_delete=models.CASCADE)
    duration = models.IntegerField(max_length=10)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Courses"


class CourseEnrollment(GenericBaseModel):
    """
    The model for holding subjects eg Maths, Eng
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Courses"


class Subject(GenericBaseModel):
    """
    The model for holding subjects eg Maths, Eng
    """
    code = models.CharField(max_length=6, default='100000')

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Subjects"

class CourseSubject(GenericBaseModel):
    """
    The model for holding CourseSubject
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Course Subjects"


class Unit(GenericBaseModel):
    """
    The model for holding units
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default='100000')

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Units"


class Notes(GenericBaseModel):
    """
    The model for holding notes
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.slug)

    class Meta(object):
        verbose_name_plural = "Notes"


class Quiz(GenericBaseModel):
    """
    The model for holding quizes
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=6, default='100000')

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Quizes"


class QuizQuestion(GenericBaseModel):
    """
    The model for holding Quiz Question
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Quiz Question"


class QuizQuestionChoices(GenericBaseModel):
    """
    The model for holding quiz question choices
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice = models.TextField()
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Quiz Question Quiz Question"

class QuizResult(GenericBaseModel):
    """
    The model for holding results for quizes
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    enrolled_student = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)
    marks = models.IntegerField(max_length=10)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Quiz Results"


class Assignment(GenericBaseModel):
    """
    The model for holding homework
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField()
    due_date = models.DateTimeField()


    def __str__(self):
        return '%s %s' % (self.name, self.code)

    class Meta(object):
        verbose_name_plural = "Assignments"
