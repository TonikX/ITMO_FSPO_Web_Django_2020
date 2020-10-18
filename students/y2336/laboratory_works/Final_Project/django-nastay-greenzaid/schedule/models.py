from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Person(AbstractUser):
    image = models.ImageField(upload_to='', default='default.jpg')
    phone = models.CharField(max_length=20)
    parent_phone = models.CharField(max_length=20, null=True, blank=True)
    citizenship = models.CharField(max_length=30)
    birthday = models.DateField()
    is_teacher = models.BooleanField(default=False)
    group = models.ForeignKey("Group", on_delete=models.SET_NULL, null=True, blank=True)
    school_grades = models.IntegerField(choices=[(9, 9), (10, 10), (11, 11)], default=9)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Group(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, choices=[('Mo', 'Понедельник'), ('Tu', 'Вторник'),
                                                   ('We', 'Среда'), ('Th', 'Четверг'),
                                                   ('Fr', 'Пятница'), ('Sa', 'Суббота')])
    lesson_number = models.CharField(max_length=10, choices=[('I', 'I'), ('II', 'II'),
                                                             ('III', 'III'), ('IV', 'IV'),
                                                             ('V', 'V'), ('VI', 'VI'),
                                                             ('VII', 'VII'), ('VIII', 'VIII')])

    def __str__(self):
        return f'{self.lesson_number}: {self.teacher} - {self.subject} ({self.group})'


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    lesson_number = models.CharField(max_length=10, choices=[('I', 'I'), ('II', 'II'),
                                                             ('III', 'III'), ('IV', 'IV'),
                                                             ('V', 'V'), ('VI', 'VI'),
                                                             ('VII', 'VII'), ('VIII', 'VIII')])

    def __str__(self):
        return f'{self.lesson_number}: {self.teacher} - {self.subject} ({self.group})'


class Grade(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return f'{self.student} {self.grade}'
