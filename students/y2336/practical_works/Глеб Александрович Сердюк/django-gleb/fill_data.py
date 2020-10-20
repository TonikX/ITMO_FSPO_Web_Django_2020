from django.core.files import File

from core import models

import random

import requests
from bs4 import BeautifulSoup
import re


def fill_brands():
    names = [
        'ALORIS', 'Эридан', 'POKROVSKY', 'Beltrami', 'gioielli', 'Vloes', 'ЮФ', 'АргентА', 'КРАСЦВЕТМЕТ', 'Zolotye',
        'Uzory', 'DARVIN', 'Дарина'
    ]
    for name in names:
        models.Brand.objects.create(name=name)


def fill_jewelry():
    regexp_name = r"name:\ +'([А-Яа-я\ ]+)'"
    regexp_image = r'mainImage:\ +"(https:\/\/g\d\.sunlight\.net\/media\/products\/[0-9A-Za-z]+\.jpg)"'

    base_url = 'https://spb.sunlight.net'
    catalog = '/catalog/'

    countries = ['Россия', 'Ураина', 'Беларусь', 'Молдова']
    metal = ['Золотое', 'Серебрянное', 'Стальное']
    jews = ['изумрудом и бриллиантами', 'алмазом', 'фионитом', 'сапфиром и изумрудом', 'бриллиантами']

    resp = requests.get(base_url + catalog)
    soup = BeautifulSoup(resp.text)
    tags = soup.find_all(class_='cl-item-link js-cl-item-link js-cl-item-root-link')
    href_list = []
    for tag in tags:
        href_list.append(tag['href'])

    for i, href in enumerate(href_list):
        resp = requests.get(base_url + href)
        names = re.findall(regexp_name, resp.text)
        if names:
            name = names[0]
        else:
            name = random.choice(metal) + ' кольцо с ' + random.choice(jews)
        # brand = re.findall(regexp_brand, resp.text)[0]
        rindex = random.randint(0, len(models.Brand.objects.all()) - 1)
        brand = models.Brand.objects.all()[rindex]

        sources = re.findall(regexp_image, resp.text)
        # print(BeautifulSoup(resp.text))
        print(name)
        if sources:
            img_src = sources[0]
        else:
            img_src = "https://g8.sunlight.net/media/products/25c69f2dd79343507ef96e22ace0957e7fd5e9f9.jpg"

        img_resp = requests.get(img_src)
        with open(f'sunlight/{i}.jpg', 'wb') as f:
            f.write(img_resp.content)

        price = random.randint(5, 50) * 1000
        number = i * 19000 + 234
        weight = random.randint(15, 30) * 0.1
        country = random.choice(countries)
        jewelry = models.Jewelry(name=name,
                                 brand=brand,
                                 price=price,
                                 number=number,
                                 weight=weight,
                                 image=File(open(f'sunlight/{i}.jpg', 'rb')),
                                 country=country)
        # jewelry.image.save(f'{i}.jpg', )
        jewelry.save()


def fill_sales():
    products = list(models.Jewelry.objects.all())[::3]
    for current_product in products:
        percent = random.randint(5, 70)
        date_start = f'2020-{random.randint(1, 5)}-{random.randint(6, 9)}'
        date_end = f'2020-{random.randint(6, 12)}-{random.randint(1, 30)}'
        models.Sale.objects.create(product=current_product, sale_percent=percent, date_start=date_start, date_end=date_end)
