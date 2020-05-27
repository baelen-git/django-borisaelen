FROM python:3-alpine
LABEL maintainer="boris@borisaelen.nl"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

#The official mirros were too slow from Thailand
#RUN echo "http://dl-5.alpinelinux.org/alpine/v3.11/main" > /etc/apk/repositories
#RUN echo "http://dl-5.alpinelinux.org/alpine/v3.11/community" >> /etc/apk/repositories
RUN apk add build-base postgresql-dev mariadb-connector-c-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del build-base 

COPY docker-entrypoint.sh docker-entrypoint.sh
COPY borisaelen borisaelen
COPY blog blog
COPY manage.py manage.py

# run entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]
#CMD python manage.py runserver 0.0.0.0:8000

