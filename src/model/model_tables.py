from datetime import datetime
import sys
import os
sys.path.append("DepoHunter_paradigmas/src")

class user_repeact(Exception):
    pass

class Lodging:
    def __init__(self, id, name, city, price,
                 type, capacity, rooms_number, bathrooms_number,
                 bedrooms_number, id_host):
        self.id = id
        self.name = name
        self.city = city
        self.price = price
        self.type = type
        self.capacity = capacity
        self.rooms_number = rooms_number
        self.bathrooms_number = bathrooms_number
        self.bedrooms_number = bedrooms_number
        self.id_host = id_host

    
    class User: #usuario
        def __init__(self, name, password):
            self.name = name
            self.password = password
        

        @staticmethod
        def checkregister(consult):
            if consult is None:
                pass
            else: 
                raise user_repeact("Ya hay un usuario registrado con este usuario")



class Reservation:
    def __init__(self, id_reservation, id_lodging, initial_date, end_date):
        self.id_reservation = id_reservation
        self.id_lodging = id_lodging
        self.initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    

class Image:
    def __init__(self,id_image,lodging,address):
        self.id_image=id_image
        self.lodging=lodging
        self.address=address
        return

class Host:
    def __init__(self,id_lodging,host_name):
        self.id_lodging
        self.host=host_name
        return
        

class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method
        self.status = False

class Review:
    def __init__(self, id_review, user, lodging, rating, comment):
        self.id_review = id_review
        self.user = user
        self.lodging = lodging
        self.rating = rating
        self.comment = comment
