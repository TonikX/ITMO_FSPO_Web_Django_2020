from rest_framework import serializers
from .models import Discipline, Student, Teacher, ExamSchedule, Exam

class DisciplineSerializer(serializers.ModelSerializer):
    """Сериализация модели Дисциплина"""

    class Meta:
        model = Discipline
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    """Сериализация модели Студент"""

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    """Сериализация модели Преподаватель"""

    class Meta:
        model = Teacher
        fields = "__all__"


class ExamScheduleSerializer(serializers.ModelSerializer):
    """Сериализация модели Расписание экзаменов"""

    class Meta:
        model = ExamSchedule
        fields = "__all__"


class ExamScheduleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для вневения новых данных в модель Расписание экзаменов"""

    class Meta:
        model = ExamSchedule
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    """Сериализация модели Экзамен"""
    discipline_discipline_code = DisciplineSerializer(many=False)
    student_gradebook_number = StudentSerializer(many=False)
    teacher_teacher_id = TeacherSerializer(many=False)
    exam_schedule_exam_id = ExamScheduleSerializer(many=False)


    class Meta:
        model = Exam
        fields = "__all__"


class ExamCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для вневения новых данных в модель Экзамен"""

    class Meta:
        model = Exam
        fields = "__all__"
