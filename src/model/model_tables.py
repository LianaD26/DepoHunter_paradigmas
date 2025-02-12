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
        self.reservations = []

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
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def check_availability(self, start_date, end_date):
        for reservation in self.reservations:
            if not reservation.get_availability(start_date, end_date):
                return False
        return True

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



print("---------------------------------------------------------------------------------------------------")

# Crear otro alojamiento
lodging_2 = Lodging(
    id=2,
    name="Apartamento en Medellín",
    city="Medellín",
    latitude=6.2442,
    longitude=-75.5812,
    price=100,
    type="Apartamento",
    capacity=4,
    rooms_number=2,
    bathrooms_number=1,
    bedrooms_number=2,
    id_host=102
)

# Crear otro usuario
user_2 = User(name="Andrea", password="clave456")

# Crear una segunda reserva
reservation_2 = Reservation(
    id_reservation=2,
    id_lodging=2,
    initial_date="2025-02-26",
    end_date="2025-03-02"
)

# Añadir la reserva al usuario y al alojamiento
user_2.add_reservation(reservation_2)

# Verificar disponibilidad antes de agregar la reserva al alojamiento
print("Disponibilidad antes de agregar la reserva:", lodging_2.check_availability(datetime(2025, 2, 27), datetime(2025, 2, 28)))

# Añadir la reserva al alojamiento
lodging_2.add_reservation(reservation_2)

# Verificar disponibilidad después de agregar la reserva al alojamiento
print("Disponibilidad después de agregar la reserva:", lodging_2.check_availability(datetime(2025, 2, 27), datetime(2025, 2, 28)))

# Crear otra imagen para el nuevo alojamiento
image_2 = Image(id_image=2, lodging=2, address="https://example.com/apartamento_medellin.jpg")

# Crear otro host
host_2 = Host(host_name="Juan Pérez")

# Crear otro pago
payment_2 = Payment(amount=100, payment_method="PayPal")
payment_2.process_payment()

# Mostrar datos del segundo alojamiento
print(str(lodging_2))

# Mostrar duración de la segunda reserva
print(f"La duración de la reserva es de {reservation_2.get_duration()} días.")

