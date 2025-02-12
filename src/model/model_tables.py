from datetime import datetime


class Lodging:
    def __init__(self, id, name, city, latitude, longitude, price,
                 type, capacity, rooms_number, bathrooms_number,
                 bedrooms_number, id_host):
        self.id = id
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.price = price
        self.type = type
        self.capacity = capacity
        self.rooms_number = rooms_number
        self.bathrooms_number = bathrooms_number
        self.bedrooms_number = bedrooms_number
        self.id_host = id_host

    def add_reservation(self, reservation):
        if self.check_availability(reservation.initial_date, reservation.end_date):
            self.reservations.append(reservation)
            print(f"Reservation {reservation.id_reservation} added succesfully")
        else:
            print(f"Reservation not added {reservation.id_reservation}, dates not available")

    def check_availability(self, start_date, end_date):
        for reservation in self.reservations:
            if not reservation.get_availability(start_date, end_date):
                return False
        return True

    def __str__(self):
        return f"Lodging {self.name} in {self.city}, price: {self.price}"

    

class User: #usuario
    def __init__(self, name, password):
        self.name = name
        self.password = password

class Reservation:
    def __init__(self, id_reservation, id_lodging, initial_date, end_date):
        self.id_reservation = id_reservation
        self.id_lodging = id_lodging
        self.initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def get_availability(self, initial_date, end_date):
        return not (initial_date < self.end_date and end_date > self.initial_date)

    def get_duration(self):
        return (self.end_date - self.initial_date).days


class Image:
    def __init__(self,id_image,lodging,address):
        self.id_image=id_image
        self.lodging=lodging
        self.address=address
        return

class Host:
    def __init__(self,host_name):
        self.host=host_name
        return
        

class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method
        self.status = False

    def process_payment(self):
        print(f"Procesing payment {self.amount} with {self.payment_method}...")
        self.status = True
        print("Succesfull payment")

class Review:
    def __init__(self, id_review, user, lodging, rating, comment):
        self.id_review = id_review
        self.user = user
        self.lodging = lodging
        self.rating = rating
        self.comment = comment
