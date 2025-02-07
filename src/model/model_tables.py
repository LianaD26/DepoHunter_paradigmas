class Lodging: #alojamiento
    def __init__(self,name
                ,city,latitude,
                length,price,
                type,capacity,
                rooms_number,bathrooms_number,
                bedrooms_number,id_host):
        self.name=name
        self.city=name
        self.latitude=latitude
        self.length=length
        self.price=price
        self.type=type
        self.capacity=capacity
        self.rooms_number=rooms_number
        self.bathrooms_number=bathrooms_number
        self.bedrooms_number=bedrooms_number
        self.id_host=id_host
    return 



class user:
    def __init__(self,name,password):
        self.name=name
        self.password=password
    return 


class reservation:
    def __init__(self,id_reservation,
                id_lodging,initial_date,end_date):
        
        self.id_reservation=id_reservation
        self.id_lodging=id_lodging
        self.initial_date=initial_date
        self.end_date=end_date
    return


class image:
    def __init__(self,id_image,lodging,address):
        self.id_image=id_image
        self.lodging=lodging
        self.address=address
    return

class host:
    def __init__(self,host):
        self.host=host
        