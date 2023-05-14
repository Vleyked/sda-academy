"""Task 1
1. Create a connection to a db
2. Create a cursor
3. Execute multiple queries to the database from your code
4. Fetch the results of all queries to the terminal
"""
import mysql.connector


def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def create_cursor(connection):
    return connection.cursor()


def execute_query(cursor, query):
    cursor.execute(query)


def fetch_results(cursor):
    return cursor.fetchall()


def print_results(results):
    for row in results:
        print(row)


def close_connection(connection):
    connection.close()


if __name__ == "__main__":
    HOST = "localhost"
    USER = "root"
    PASSWORD = "root"
    DATABASE = "store"

    queries = [
        "SELECT * FROM customers;",
        "SELECT * FROM orders;",
        "SELECT * FROM products;",
        "SELECT * FROM reviews;",
        "SELECT * FROM users;",
    ]

    for query in queries:
        # Step 1: Create a connection to the database
        connection = connect_to_database(HOST, USER, PASSWORD, DATABASE)
        # Step 2: Create a cursor
        cursor = create_cursor(connection)
        # Step3: Execute multiple queries
        execute_query(cursor, query)
        # Step 4: Fetch the results and print it ot the terminal
        results = fetch_results(cursor)
        print_results(results)
        # Step 5: Close the connection
        close_connection(connection)
