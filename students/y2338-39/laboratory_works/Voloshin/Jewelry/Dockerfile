FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY manage.py /code/
COPY lab_vol_final /code/lab_vol_final
COPY db.sqlite3 /code/
COPY final_app /code/final_app