import MySQLdb

user = '<user>'
password = '<pass>'

db = MySQLdb.connect(user=user, password=password, database='music')

def get_instruments_count(connection):
    get_count_sql = """"""
    cursor = connection.cursor(MySQLdb.cursors.'Choose a cursor type')
    cursor.execute(get_count_sql)
    return cursor.fetchall()

with db:
    result = get_instruments_count(db)