import MySQLdb

user = '<user>'
password = '<pass>'

db = MySQLdb.connect(user=user, password=password)

create_database = """CREATE DATABASE IF NOT EXISTS music;USE music;"""
create_tables = """
CREATE TABLE instruments(
    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    family VARCHAR(30) NOT NULL,
    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
);
"""

with db:
    cursor = db.cursor()
    cursor.execute(create_database)
    cursor.execute(create_tables)