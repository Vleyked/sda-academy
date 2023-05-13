FROM mysql:latest

# Create database and user
ENV MYSQL_DATABASE store
ENV MYSQL_USER mysql_user
ENV MYSQL_PASSWORD mysql_password

# Copy the SQL files into the container's /docker-entrypoint-initdb.d directory
COPY create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
COPY insert_data.sql /docker-entrypoint-initdb.d/insert_data.sql

# Map container port 3306 to host system port 3306
EXPOSE 3306

# Start MySQL server in the foreground
CMD ["mysqld", "--default-authentication-plugin=mysql_native_password", "--user=mysql"]
