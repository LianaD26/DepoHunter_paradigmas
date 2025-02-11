from datetime import datetime


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
        
    def add_reservation(self, reservation):
        self.reservations.append(reservation)

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
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def check_availability(self, start_date, end_date):
        for reservation in self.reservations:
            if not reservation.get_availability(start_date, end_date):
                return False
        return True

class Reservation:
    def __init__(self,id_reservation,
                id_lodging,initial_date,end_date):
        
        self.id_reservation=id_reservation
        self.id_lodging=id_lodging
        self.initial_date= datetime.strptime(initial_date, '%Y-%m-%d')
        self.end_date= datetime.strptime(end_date, '%Y-%m-%d')
    
    def get_availability(self, initial_date, end_date):
        if initial_date < self.end_date and end_date > self.initial_date:
            return False
        return True
    
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
    


# Crear un alojamiento
try:
    lodging_1 = Lodging(
        id=1,
        name="Casa de playa",
        city="Cartagena",
        latitude=10.3910,
        longitude=-75.4796,
        price=150,
        type="Casa",
        capacity=6,
        rooms_number=3,
        bathrooms_number=2,
        bedrooms_number=3,
        id_host=101
    )
except ValueError as e:
    print(e)

# Crear un usuario
user_1 = User(name="Carlos", password="secreta123")

# Crear una reserva
try:
    reservation_1 = Reservation(
        id_reservation=1,
        id_lodging=1,
        initial_date="2025-02-20",
        end_date="2025-02-25"
    )
except ValueError as e:
    print(e)

# Añadir la reserva al usuario
user_1.add_reservation(reservation_1)

# Verificar disponibilidad
print("Disponibilidad para la fecha:", reservation_1.get_availability(datetime(2025, 2, 22), datetime(2025, 2, 24)))

# Crear una imagen de un alojamiento
image_1 = Image(id_image=1, lodging=1, address="https://example.com/casa_playa.jpg")

# Crear un host
host_1 = Host(host_name="Ana María")

# Crear un pago
payment_1 = Payment(amount=150, payment_method="tarjeta de crédito")
payment_1.process_payment()

# Mostrar datos de un alojamiento
print(str(lodging_1))

# Mostrar duración de la reserva
print(f"La duración de la reserva es de {reservation_1.get_duration()} días.")
