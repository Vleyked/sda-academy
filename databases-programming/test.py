from mysql.connector import connect, Error

try:
    with connect(
        host="localhost", user="root", password="toor", database="online_movie_rating"
    ) as conn:
        sql_statement = """

        SELECT title FROM movies WHERE title = 'Dude where is my car?'
        ;
        """
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            # conn.commit()
            result = cursor.fetchmany(5)
            for row in result:
                print(row)

        print("Code executed successfully!")

except Error as e:
    print(e)

# , database="online_movie_rating"
