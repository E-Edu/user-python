FROM python:3.8.2
COPY . /microservice/
WORKDIR /microservice/
RUN pip install --upgrade pip

RUN apk add --update libxml2-dev libxslt-dev gcc g++ bash vim nano
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/main.py"]