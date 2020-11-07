from django_filters import rest_framework as filters
from .models import Student, Teacher


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class StudentFilter(filters.FilterSet):
    course = CharFilterInFilter(field_name='course', lookup_expr='in')
    group_number = CharFilterInFilter(field_name='group_number', lookup_expr='in')


    class Meta:
        model = Student
        fields = ['course', 'group_number']


class TeacherFilter(filters.FilterSet):
    department = CharFilterInFilter(field_name='department', lookup_expr='in')


    class Meta:
        model = Teacher
        fields = ['department']