FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY manage.py /code/
COPY perfumeerie /code/perfumeerie
COPY perfum /code/perfum

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]