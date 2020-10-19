FROM python:3.7.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN mkdir -p /var/log/platform_admin

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r ins.txt
RUN pip install django-widget-tweaks
RUN python manage.py makemigrations
RUN python manage.py migrate