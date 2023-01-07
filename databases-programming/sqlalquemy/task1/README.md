# Task 1
Let's introduce relationships to the database - one to many:

one car -> many reservations, one reservation -> one car
one client -> many reservations, one reservation -> one client

Add the necessary code in the classes Clients, Cars, Bookings to bind them with the mentioned relations. 

Relationships should be bidirectional - from the level of the Cars instance, we should access theBookings instance via the bookings property. 

Similarly for the instance of the class Clients. Additionally, it is worth checking the behavior when deleting related records. Ultimately, we'd like to update the bookings table when we remove a record from theclients or cars table. Implement this mechanism.