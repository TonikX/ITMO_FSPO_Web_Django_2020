from django.db import models
from datetime import date


class Discipline(models.Model):
    discipline_code = models.IntegerField('Код дисциплины')
    discipline_name = models.CharField("Название дисциплины", max_length=100)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.discipline_name


class Student(models.Model):
    gradebook_number = models.IntegerField('Номер зачётной книжки')
    student_surname = models.CharField("Фамилия студента", max_length=100)
    student_name = models.CharField("Имя студента", max_length=100)
    middle_name_of_the_student = models.CharField("Отчество студента", max_length=100)
    course_number = models.IntegerChoices('course_number', '1 2 3 4 5')
    course = models.IntegerField('Курс', blank=True, null = True, choices=course_number.choices)
    group_number = models.IntegerField('Номер группы')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


    def __str__(self):
        return self.student_surname + ' ' + self.student_name + ' ' + self.middle_name_of_the_student


class Teacher(models.Model):
    teacher_id = models.IntegerField('ID преподавателя')
    surname_of_the_teacher = models.CharField("Фамилия преподавателя", max_length=100)
    teacher_name = models.CharField("Имя преподавателя", max_length=100)
    teacher_middle_name = models.CharField("Отчество преподавателя", max_length=100)
    department_name = models.TextChoices('department_name', 'Беспроводные_телекоммуникации Высшая_математика Инстранные_языки '
                            'Психология Менеджмент Информатика_и_прикладная_математика')
    department = models.CharField("Кафедра", blank=True, null = True, choices=department_name.choices, max_length=100)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.surname_of_the_teacher +' '+ self.teacher_name + ' ' + self.teacher_middle_name + ' ' + self.department


class ExamSchedule(models.Model):
    exam_id = models.IntegerField('ID экзамена')
    complition_date_exam = models.DateField('Дата проведения экзамена', default=date.today)
    the_audience = models.IntegerField('Номер аудитории')
    group_number = models.IntegerField('Номер группы')

    class Meta:
        verbose_name = 'Расписание экзаменов'
        verbose_name_plural = 'Расписание экзаменов'


class Exam(models.Model):
    exam_id = models.IntegerField('ID экзамена')
    assessment_n = models.IntegerChoices('assessment_n', '2 3 4 5')
    assessment = models.IntegerField('Оценка за экзамен', blank=True, null = True, choices=assessment_n.choices)
    discipline_discipline_code = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    student_gradebook_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    exam_schedule_exam_id = models.ForeignKey(ExamSchedule, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

