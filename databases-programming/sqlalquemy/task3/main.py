import MySQLdb

user = '<user>'
password = '<pass>'

db = MySQLdb.connect(user=user, password=password, database='music')

def insert_instruments(connection, instrument_values):
    # Your code here


instruments = []
with db:
    insert_instruments(db,
                       instruments)