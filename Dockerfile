FROM python:3-alpine
LABEL maintainer="boris@borisaelen.nl"
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

#The official mirros were too slow from Thailand
#RUN echo "http://dl-5.alpinelinux.org/alpine/v3.11/main" > /etc/apk/repositories
#RUN echo "http://dl-5.alpinelinux.org/alpine/v3.11/community" >> /etc/apk/repositories
RUN apk add mariadb-dev build-base postgresql-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY borisaelen borisaelen
COPY blog blog
COPY manage.py manage.py

CMD python manage.py runserver 0.0.0.0:8000
