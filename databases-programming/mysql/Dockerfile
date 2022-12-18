# Mysql Dockerfile
FROM mysql:5.7

LABEL maintainer "vleyked"

ENV MYSQL_ROOT_PASSWORD=toor
ENV MYSQL_DATABASE=sda
ENV MYSQL_USER=test
ENV MYSQL_PASSWORD=test

COPY create_online_movie_database.sql /docker-entrypoint-initdb.d/

EXPOSE 3306