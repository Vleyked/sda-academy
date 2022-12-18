from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="root", password="toor", database="online_movie_rating"
    ) as conn:
        sql_statement = """
        SELECT 1;
        """
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            conn.commit()

except Error as e:
    print(e)
