class Lodging: #alojamiento
    def __init__(self, id, name
                ,city,latitude,
                longitude,price,
                type,capacity,
                rooms_number,bathrooms_number,
                bedrooms_number,id_host):
        self.id=id
        self.name=name
        self.city=city
        self.latitude=latitude
        self.longitude=longitude
        self.price=price
        self.type=type
        self.capacity=capacity
        self.rooms_number=rooms_number
        self.bathrooms_number=bathrooms_number
        self.bedrooms_number=bedrooms_number
        self.id_host=id_host
        return
    

class User: #usuario
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

        return 


class Reservation:
    def __init__(self,id_reservation,
                id_lodging,initial_date,end_date):
        
        self.id_reservation=id_reservation
        self.id_lodging=id_lodging
        self.initial_date=initial_date
        self.end_date=end_date
        return
    
    def get_availability(self, start_date, end_date):
        for reservation in self.reservations:
            if (start_date < reservation.end_date and end_date > reservation.start_date):
                return False
        return True


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
    def __init__(self, payment):
        self.payment = payment
        return