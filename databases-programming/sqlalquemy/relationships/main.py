from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import relationship

#TODO: Task 1
'''
Let's introduce relationships to the database - one to many:

one car -> many reservations, one reservation -> one car
one client -> many reservations, one reservation -> one client
Add the necessary code in the classes Clients, Cars, Bookings 
to bind them with the mentioned relations. 

Relationships should be bidirectional - from the level of the Cars instance, 
we should access theBookings instance via the bookings property. Similarly 
for the instance of the class Clients. 

Additionally, it is worth checking the behavior when deleting related records. 

Ultimately, we'd like to update the bookings table when we remove a 
record from theclients or cars table. Implement this mechanism.
'''

class Cars(base):
    __tablename__ = 'cars'
    # Your code here
    def __repr__(self):
        return f"<Car: id={self.car_id}, producer={self.producer}, model={self.model}, year={self.year}, " \
               f"horse_power={self.horse_power}, price_per_day={self.price_per_day}>"

class Clients(base):
    __tablename__ = 'clients'

    # Your code here

    def __repr__(self):
        return f"<Client: id={self.client_id}, name={self.name}, surname={self.surname}, address={self.address}," \
               f"city={self.city}>"

class Bookings(base):
    __tablename__ = 'bookings'

    # Your code here

    def __repr__(self):
        return f"<Booking: id={self.booking_id}, client_id={self.client_id}, car_id={self.car_id}, " \
               f"start_date={self.start_date}, end_date={self.end_date}, total_amount={self.total_amount}>"


# Task 2
"""
We need your data to be able to carry out a series of queries. 

Write a function insert_data that will take arguments:

base - the base class of the model we want to create an instance of
params - dictionary with specific parameters of the created object
Test the function against the provided data:
"""

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
    # Your code here

for client in clients:
    insert_data() # Complete the code
for car in cars:
    insert_data() # Complete the code
for booking in bookings:
    insert_data() # Complete the code

