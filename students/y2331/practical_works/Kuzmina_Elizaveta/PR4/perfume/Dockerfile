FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /back
WORKDIR /back
COPY req.txt /back/
RUN pip install -r req.txt
COPY manage.py /back/
COPY perfume /back/perfume
COPY db.sqlite3 /back/
COPY perfume_app /back/perfume_app
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]