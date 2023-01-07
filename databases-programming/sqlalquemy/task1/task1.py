from sqlalchemy.orm import relationship


class Cars(base):
    __tablename__ = "cars"
    # Write your code here.
    def __repr__(self):
        return (
            f"<Car: id={self.car_id}, producer={self.producer}, model={self.model}, year={self.year}, "
            f"horse_power={self.horse_power}, price_per_day={self.price_per_day}>"
        )


class Clients(base):
    __tablename__ = "clients"
    # Write your code here.
    def __repr__(self):
        return (
            f"<Client: id={self.client_id}, name={self.name}, surname={self.surname}, address={self.address},"
            f"city={self.city}>"
        )


class Bookings(base):
    __tablename__ = "bookings"
    # Write your code here.
    def __repr__(self):
        return (
            f"<Booking: id={self.booking_id}, client_id={self.client_id}, car_id={self.car_id}, "
            f"start_date={self.start_date}, end_date={self.end_date}, total_amount={self.total_amount}>"
        )
