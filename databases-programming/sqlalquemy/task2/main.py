import MySQLdb


def est_connection():
    """
    Establish connection to the SQL database
    """
    user = 'root'
    password = 'root'

    db = MySQLdb.connect(user=user, password=password)
    return db


# Variable for working with the MySQL connection
CONNECTION = est_connection()

# A mock database of instruments that we insert into our db later
INSTRUMENTS = [
    ['YAMAHA TRBX204', 'Bass Guitar', 'difficult'],
    ['Pearl Midtown 4', 'Drum Set', 'hard'],
    ['Roland VR-09-B', 'Synthesizer', 'hard']
]


def create_db():
    """
    Create our database if it has not been created yet
    """
    create_database = (
        "CREATE DATABASE IF NOT EXISTS music;"
    )
    with CONNECTION.cursor() as cursor:
        cursor.execute("USE music;")
        cursor.execute(
            create_database
        )
        cursor.close()


def create_table():
    """
    Create our table if it has not been created yet
    """
    create_table = (
                    "CREATE TABLE IF NOT EXISTS `Instruments` (instrument_id INT PRIMARY KEY AUTO_INCREMENT,"
                    "name VARCHAR(255),"
                    "family VARCHAR(255),"
                    "difficulty ENUM('easy','difficult','hard'));"
    )
    with CONNECTION.cursor() as cursor:
        cursor.execute(
            create_table
        )
        cursor.close()


def insert_into_db(data):
    """
    We use our mock data list to insert its values into the database
    """
    with CONNECTION.cursor() as cursor:
        insert_values = """INSERT INTO `Instruments` (name, family, difficulty)
        VALUES (%s, %s, %s);"""
        for indx in range(0, 3):
            cursor.execute(
                insert_values, (data[indx][0], data[indx][1], data[indx][2])
            )
        CONNECTION.commit()


if __name__ == "__main__":
    create_db()
    create_table()
    insert_into_db(INSTRUMENTS)
