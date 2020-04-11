from django.urls import path
from . import views  # подключение файла контроллеров,описанного в пункте 3
from .views import detail

urlpatterns = [
    # пример вызова контроллера (функции) с именем "special_case_200" из файда views
    path('<int:owner>/', detail, name='owner'),
    # пример вызова контроллера (функции) с именем "year_archive" из файда viewsи передачи в него переменной "year"
]
