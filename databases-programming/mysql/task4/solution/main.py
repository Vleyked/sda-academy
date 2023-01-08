import MySQLdb

user = '<user>'
password = '<pass>'

db = MySQLdb.connect(user=user, password=password, database='music')

def get_instruments_count(connection):
    get_count_sql = """SELECT family, count(*) as count FROM instruments GROUP BY family;"""
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(get_count_sql)
    return cursor.fetchall()

with db:
    result = get_instruments_count(db)