FROM python:3

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY ./manage.py ./
COPY ./pyproj ./pyproj
COPY ./pyapp ./pyapp

RUN python ./manage.py migrate
