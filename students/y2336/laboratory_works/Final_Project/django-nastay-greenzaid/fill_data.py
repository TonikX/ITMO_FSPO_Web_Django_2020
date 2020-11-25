from schedule import models

import random


def fill_schedule():
    # subjects = ['Высшая математика',
    #             'Программирование программных модулей',
    #             'Основы проектирования баз данных',
    #             'Веб программирование',
    #             'Основы дизайна',
    #             'Тестирование и разработка программного обеспечения',
    #             'Разработка мобильных приложений',
    #             'UI/UX',
    #             'Основы машинного обучения']
    # for subject in subjects:
    #     models.Subject.objects.create(name=subject)
    #
    # number_form = '+7(911){}-{}-{}'
    # for _ in range(20):
    #     number = number_form.format(random.randint(100, 999),
    #                                 random.randint(10, 99),
    #                                 random.randint(10, 99))
    #     birthday = f'19{random.randint(85, 99)}-{random.randint(1, 12)}-{random.randint(1, 28)}'
    #     models.Person.objects.create(
    #         username=str(_),
    #         phone=number,
    #         citizenship='ДНР',
    #         birthday=birthday,
    #         is_teacher=True
    #     )
    #
    # for i in range(1, 3):
    #     for j in range(4):
    #         number = i * 100 + j
    #         models.ClassRoom.objects.create(number=number)
    group = models.Group.objects.get(number='Y2436')
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

    lessons_number = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

    teachers = models.Person.objects.filter(is_teacher=True)
    for day in days:
        number_of_lessons = random.randint(3, 8)
        for ln in range(number_of_lessons):
            rindex = random.randint(0, len(models.Subject.objects.all()) - 1)
            subject = models.Subject.objects.all()[rindex]

            rindex = random.randint(0, len(teachers.all()) - 1)
            teacher = teachers.all()[rindex]

            models.Schedule.objects.create(group=group,
                                           subject=subject,
                                           teacher=teacher,
                                           day=day,
                                           lesson_number=lessons_number[ln])


def fill_lessons():
    group = models.Group.objects.get(number='Y2436')
    schedule = models.Schedule.objects.filter(group=group)
    start_date = '2020-10-{}'
    current_day = 5
    for i in range(len(schedule) - 1):
        models.Lesson.objects.create(
            group=group,
            subject=schedule[i].subject,
            teacher=schedule[i].teacher,
            date=start_date.format(current_day),
            lesson_number=schedule[i].lesson_number
        )
        if schedule[i].day != schedule[i + 1].day:
            current_day += 1

    models.Lesson.objects.create(
        group=group,
        subject=schedule[-1].subject,
        teacher=schedule[-1].teacher,
        date=start_date.format(i),
        lesson_number=schedule[-1].lesson_number
    )
