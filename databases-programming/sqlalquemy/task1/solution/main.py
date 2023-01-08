from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
import datetime

eng = create_engine('mysql://user:password@localhost:3306/car_rental')

base = declarative_base()

class Cars(base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)

class Clients(base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)

class Bookings(base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, nullable=False)
    car_id = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)

base.metadata.create_all(eng)

Session = sessionmaker(bind=engine)
session = Session()

# Bellow code will only return values if the requested data exist in the tables
car_1 = Cars(producer='BMW', model='X6', year=2020, horse_power=5000, price_per_day=50)
car_1_sql_eq = """
SELECT * from cars
WHERE producer == 'BMW'
AND model == 'X6'
AND year == 2020
AND horse_power == 5000
AND price_per_day == 50
"""

client_1 = Clients(name='Hugh', surname='Mungus', address='Viru tn. 1', city='Valga')
client_1_sql_eq = """
SELECT * from cars
WHERE producer == 'BMW'
AND model == 'X6'
AND year == 2020
AND horse_power == 5000
AND price_per_day == 50
"""

booking_1 = Bookings(client_id=191334, car_id=234483, start_date=datetime.datetime.now(),
                     end_date=datetime.datetime.now())
booking_1_sql_eq = """
SELECT * from bookings
WHERE client_id == 191334
AND car_id == 234483
AND start_date == -- Example: <datatime now> => 2023-01-08 09:09:20.430322
AND end_date == -- Example <datatime now> => 2023-01-08 09:09:20.430322
"""