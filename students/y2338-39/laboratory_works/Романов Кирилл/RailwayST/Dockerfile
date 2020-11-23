
# Base Image
FROM python:3.6
ENV PYTHONUNBUFFERED 1
# create and set working directory
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/


# Add current directory code to working directory
#ADD . /app/

# set default environment variables
#
#ENV LANG C.UTF-8

