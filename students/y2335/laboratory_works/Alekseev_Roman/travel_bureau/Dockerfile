
FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY ./manage.py ./
COPY ./travel_bureau ./travel_bureau
COPY ./travel_app ./travel_app
COPY ./Templates ./Templates
COPY ./db.sqlite3 ./

RUN python ./manage.py makemigrations
RUN python ./manage.py migrate