FROM python:3.8.2-alpine3.10

EXPOSE 80

COPY . /microservice/
WORKDIR /microservice/
RUN pip install --upgrade pip

RUN apk add --update libxml2-dev libxslt-dev gcc g++ bash
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
