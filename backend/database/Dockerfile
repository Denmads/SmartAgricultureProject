#docker build -t db .
#docker run -d --name data -p 3306:3306 db
FROM mysql

ENV MYSQL_ROOT_PASSWORD password
ENV MYSQL_DATABASE hub

ADD schema.sql /docker-entrypoint-initdb.d

#docker exec -it data bash