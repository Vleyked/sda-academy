from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

user = ''
password = ''
host = ''
port = ''
db_type = '' # mysql, postgresql...
db_name = ''

engine = create_engine(f'{db_type}://{user}:{password}@{host}:{port}/{db_name}')

class Clients(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    address = Column(String)
    city = Column(String)

class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    producer = Column(String)
    model = Column(String)
    year = Column(Integer)
    horse_power = Column(Integer)
    price_per_day = Column(Integer)

class Bookings(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    car_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    total_amount = Column(Integer)

clients = [
    {'name': 'Jan', 'surname': 'Kowalski', 'address': 'ul. Florianska 12', 'city': 'Krakow'},
    {'name': 'Andrzej', 'surname': 'Nowak', 'address': 'ul. Saska 43', 'city': 'Wroclaw'},
    {'name': 'Michal', 'surname': 'Taki', 'address': 'os. Srodkowe 12', 'city': 'Poznan'},
    {'name': 'Pawel', 'surname': 'Ktory', 'address': 'ul. Stara 11', 'city': 'Gdynia'},
    {'name': 'Anna', 'surname': 'Inna', 'address': 'os. Srednie 1', 'city': 'Gniezno'},
    {'name': 'Alicja', 'surname': 'Panna', 'address': 'os. Duze 33', 'city': 'Torun'},
    {'name': 'Damian', 'surname': 'Papa', 'address': 'ul. Skosna 66', 'city': 'Warszawa'},
    {'name': 'Marek', 'surname': 'Troska', 'address': 'os. Male 90', 'city': 'Radom'},
    {'name': 'Jakub', 'surname': 'Klos', 'address': 'os. Polskie 19', 'city': 'Wadowice'},
    {'name': 'Lukasz', 'surname': 'Lis', 'address': 'os. Podlaskie 90', 'city': 'Bialystok'}]
cars = [
    {'producer': 'Seat', 'model': 'Leon', 'year': 2016, 'horse_power': 80, 'price_per_day': 200},
    {'producer': 'Toyota', 'model': 'Avensis', 'year': 2014, 'horse_power': 72, 'price_per_day': 100},
    {'producer': 'Mercedes', 'model': 'CLK', 'year': 2018, 'horse_power': 190, 'price_per_day': 400},
    {'producer': 'Hyundai', 'model': 'Coupe', 'year': 2014, 'horse_power': 165, 'price_per_day': 300},
    {'producer': 'Dacia', 'model': 'Logan', 'year': 2015, 'horse_power': 103, 'price_per_day': 150},
    {'producer': 'Saab', 'model': '95', 'year': 2012, 'horse_power': 140, 'price_per_day': 140},
    {'producer': 'BMW', 'model': 'E36', 'year': 2007, 'horse_power': 110, 'price_per_day': 80},
    {'producer': 'Fiat', 'model': 'Panda', 'year': 2016, 'horse_power': 77, 'price_per_day': 190},
    {'producer': 'Honda', 'model': 'Civic', 'year': 2019, 'horse_power': 130, 'price_per_day': 360},
    {'producer': 'Volvo', 'model': 'XC70', 'year': 2013, 'horse_power': 180, 'price_per_day': 280}]
bookings = [
    {'client_id': 3, 'car_id': 3, 'start_date': '2020-07-06', 'end_date': '2020-07-08', 'total_amount': 400},
    {'client_id': 6, 'car_id': 10, 'start_date': '2020-07-10', 'end_date': '2020-07-16', 'total_amount': 1680},
    {'client_id': 4, 'car_id': 5, 'start_date': '2020-07-11', 'end_date': '2020-07-14', 'total_amount': 450},
    {'client_id': 5, 'car_id': 4, 'start_date': '2020-07-11', 'end_date': '2020-07-13', 'total_amount': 600},
    {'client_id': 7, 'car_id': 3, 'start_date': '2020-07-12', 'end_date': '2020-07-14', 'total_amount': 800},
    {'client_id': 5, 'car_id': 7, 'start_date': '2020-07-14', 'end_date': '2020-07-17', 'total_amount': 240},
    {'client_id': 3, 'car_id': 8, 'start_date': '2020-07-14', 'end_date': '2020-07-16', 'total_amount': 380},
    {'client_id': 5, 'car_id': 9, 'start_date': '2020-07-15', 'end_date': '2020-07-18', 'total_amount': 1080},
    {'client_id': 6, 'car_id': 10, 'start_date': '2020-07-16', 'end_date': '2020-07-20', 'total_amount': 1120},
    {'client_id': 8, 'car_id': 1, 'start_date': '2020-07-16', 'end_date': '2020-07-19', 'total_amount': 600},
    {'client_id': 9, 'car_id': 2, 'start_date': '2020-07-16', 'end_date': '2020-07-21', 'total_amount': 500},
    {'client_id': 10, 'car_id': 6, 'start_date': '2020-07-17', 'end_date': '2020-07-19', 'total_amount': 280},
    {'client_id': 1, 'car_id': 9, 'start_date': '2020-07-17', 'end_date': '2020-07-19', 'total_amount': 720},
    {'client_id': 3, 'car_id': 7, 'start_date': '2020-07-18', 'end_date': '2020-07-21', 'total_amount': 240},
    {'client_id': 5, 'car_id': 4, 'start_date': '2020-07-18', 'end_date': '2020-07-22', 'total_amount': 1200}]

def insert_data(session, base, params):
    '''Helper function to insert data into the tables'''
    session.add(base(**params))
    session.commit()


Session = sessionmaker(bind=engine)
session = Session()

# Inserting all the values
for client in clients:
    insert_data()# Complete the code
for car in cars:
    insert_data()# Complete the code
for booking in bookings:
    insert_data()# Complete the code


# Task 3
# List all reservations for the client with id = 3. Try with both query () and select ().
#1
result = session.query(Bookings).filter(Bookings.client_id == 3)
for booking in result:
    print(booking)
#2
from sqlalchemy.sql import select

conn = eng.connect()
s = select([Bookings]).where(Bookings.client_id == 3)
result = conn.execute(s).fetchall()
print(result)

# Task 4
# List all cars rented by the customer with id = 5. Cars can repeat themselves, we mean the rental history. Try with both query () and select ().

#1
result = session.query(Clients).filter_by(client_id=5)
for client in result:
    for booking in client.bookings:
        print(booking.car)

#2
result = session.query(Bookings).filter_by(client_id=5)
for booking in result:
    print(booking.car)

#3
from sqlalchemy.sql import select
from sqlalchemy import join

j = join(Bookings, Cars, Bookings.car_id == Cars.car_id)
s = select([Cars]).select_from(j).where(Bookings.client_id == 5)
result = conn.execute(s)
for car in result:
    print(car)

# Task 5
# List the id of all customers and the booking costs incurred by them, which are greater than 1100 and the bookings started after 13/07/2020 (>=14/08/2020).

from sqlalchemy import and_

result = (
    session.query(Clients.client_id, Bookings.total_amount)
    .join(Bookings)
    .filter(and_(Bookings.total_amount > 1100, Bookings.start_date >= "2020-07-14"))
    .all()
)

print(result)

# Task 6
# List the total cost of all bookings for each customer, customer name and surname for bookings that were made between 10-17/07/2020.

from sqlalchemy.sql import func

bookings_info = session.query(
    func.sum(Bookings.total_amount), Clients.name, Clients.surname
    ).join(
        Clients
    ).filter(
        and_(Bookings.start_date >= '2020-07-10', Bookings.end_date <= '2020-07-17')
    ).group_by(
        Clients.client_id
    ).all()

print(bookings_info)

# Task 7
# Write query smt in SQL and pass it to the query () function. smt should return the id of reservations for which the reservation value is greater than the value given to the main query as a parameter.

from sqlalchemy.sql import text

stm = text('SELECT booking_id FROM bookings WHERE total_amount > :amount')
result = session.query(Bookings).from_statement(stm).params(amount=200).all()
print(result)