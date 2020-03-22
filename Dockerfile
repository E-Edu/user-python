FROM python:3.7-alpine

EXPOSE 80

COPY . /microservice/
WORKDIR /microservice/
RUN apk add gcc musl-dev libffi-dev libressl-dev gnupg --update libxml2-dev libxslt-dev  g++ bash
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--workers", "4", "wsgi:application", "--bind", "0.0.0.0:80", "--log-syslog", "--log-level", "DEBUG"]