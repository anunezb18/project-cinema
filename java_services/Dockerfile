FROM openjdk:17-jdk-slim

WORKDIR /app

COPY target/java_services-0.0.1-SNAPSHOT.jar /app/java_services.jar

EXPOSE 8001

ENTRYPOINT ["java", "-jar", "java_services.jar"]