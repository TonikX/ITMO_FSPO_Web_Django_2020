from django.shortcuts import render

from django.http import \
    Http404, \
    HttpResponse  # импортирует метод обработки ситуации, когда нет    необходимых записей в бд (обработчик ошибок)
from django.shortcuts import \
    render  # импортирует метод, который "запускает" созданную хтмл страницу и передает в нее указанные параметры
from project_first_app.models import \
    CarOwner  # импортирует таблицу Poll из модели данных models, где polls - название приложения (и папки)


def detail(request, owner):
    try:  # метод try-except - обработчик исключений
        p = CarOwner.objects.get(pk=owner)  # pk - автоматически создается в джанго для любой таблицы в моделе
        # (оно есть у любого объекта из бд),
        # poll_id будет передан функции при её вызове.
    # переменной p присваивается объект, полученный в результате выполнения запроса аналогичного
    # "select * from Poll where pk=poll_id"
    except CarOwner.DoesNotExist:
        raise Http404(
            "Car owner does not exist")  # исключение которое будет вызвано, если блок try вернет значение
        # False (не будут найдены записи в таблице Poll)
    return render(request, 'owner.html', {
        'CarOwner': p})  # данная строка рендерит хтмл страницу detail.html и передает в него объект "p",
    # который в хтмл шаблоне будет называться "poll"

# Create your views here.
