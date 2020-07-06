FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY manage.py /code/
COPY FinalPetrov /code/FinalPetrov
COPY db.sqlite3 /code/
COPY turist /code/turist
COPY templates /code/templates

#CMD {"python3", "manage.py", "runserver", "0.0.0.0:8000"}