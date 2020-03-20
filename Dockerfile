FROM adoptopenjdk/openjdk11:alpine-jre

WORKDIR /eedu

COPY /target/user-microservice-0.0.1-SNAPSHOT.jar userms.jar

RUN apk --update --no-cache add tzdata \
  && cp /usr/share/zoneinfo/UTC /etc/localtime \
  && echo "UTC" >/etc/timezone \
  && apk --no-cache del tzdata

ENTRYPOINT ["java", "-jar", "userms.jar"]
