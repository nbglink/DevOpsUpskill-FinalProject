FROM adoptopenjdk/openjdk11:x86_64-ubuntu-jre-11.0.18_10

EXPOSE 9090

COPY ./target/demo-app-jma-11.jar /usr/app/
WORKDIR /usr/app

ENTRYPOINT ["java", "-jar", "demo-app-jma-11.jar"]