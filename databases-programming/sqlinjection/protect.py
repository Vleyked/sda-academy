from mysql.connector import connect, Error

try:

    SQL_QUERY = """
    UPDATE employees SET first_name = %s WHERE emp_no = %s;
    SELECT first_name FROM employees where emp_no = %s;
    """
    name, number = input("Podaj imie pracownika"), input("Podaj numer pracownika")
    values_as_tuple = (name, number, number)

    with connect(
        host="localhost", user="test", password="test", database="employees"
    ) as conn:
        cursor = conn.cursor()
        for result in cursor.execute(SQL_QUERY, values_as_tuple, multi=True):
            if result.with_rows:
                print(result.fetchall())
        conn.commit()


except Error as e:
    print(e)
