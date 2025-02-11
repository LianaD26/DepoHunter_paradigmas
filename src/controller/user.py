from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("DepoHunter_paradigmas/src")
import controller.SecretConfig as secretconfig
import model.model_tables as models 


class BaseController:
    
    def __init__(self):
        self.connection = self._GetConnection()
    
    def _GetConnection(self):
        try:
            connection = psycopg2.connect(
                dbname=secretconfig.PGDATABASE,
                user=secretconfig.PGUSER,
                password=secretconfig.PGPASSWORD,
                host=secretconfig.PGHOST,
                port=secretconfig.PGPORT
            )
            return connection
        except psycopg2.Error as e:
            print("Error al conectar con la base de datos:", e)
            sys.exit(1)

    def CreateTable(self, query):
        try:
            cursor_lodging = self.connection.cursor()
            cursor_lodging.execute(query)
            self.connection.commit()
            print("Tabla creada exitosamente.")
        except psycopg2.Error as e:
            print("Error al crear la tabla:", e)
        finally:
            cursor_lodging.close()

    def DeleteTable(self, query):
        try:
            cursor_lodging = self.connection.cursor()
            cursor_lodging.execute(query)
            self.connection.commit()
            print("Tabla borrada exitosamente.")
        except psycopg2.Error as e:
            print("Error al borrar la tabla:", e)
        finally:
            cursor_lodging.close()

    
    def PostTable(self, query, data):
        try:
            data_frame = pd.read_csv(data)
            cursor_lodging = self.connection.cursor()
            data_tuples = list(data_frame.itertuples(index=False, name=None))
            execute_values(cursor_lodging, query, data_tuples)
            self.connection.commit()
            print("Datos subidos exitosamente.")
        
        except psycopg2.Error as e:
            print("Error al cargar datos en la base de datos:", e)

        except Exception as e:
            print("Error inesperado:", e)

        finally:
            if 'cursor_lodging' in locals():
                cursor_lodging.close()
    
    def PostTableOneElement(self,query):
        try: 
            cursor_lodging = self.connection.cursor()
            cursor_lodging.execute(query)
            self.connection.commit()
            print("Elemento insertado exitosamente.")
        except psycopg2.Error as e:
            print("Error al insertar elemento en la tabla:", e)
        finally:
            cursor_lodging.close()
    
    
    def UpdateTable():
        pass     
    def Gettable():
        pass
                
class ControllerLodging:
    def __init__(self):
        self.base_controller = BaseController()

    def CreateTableLodging(self):
        query = """CREATE TABLE IF NOT EXISTS lodging (
                    id serial primary key,
                    name varchar(50) not null,
                    city varchar(50) not null,
                    latitude varchar(50) not null,
                    longitude varchar(50) not null,
                    price int not null,
                    type varchar(50) not null,
                    capacity int not null,
                    rooms_number int not null,
                    bathrooms_number int not null,
                    bedrooms_number int not null,
                    id_host int not null);"""
        self.base_controller.CreateTable(query)

    def DeleteTableLodging(self):
        query = "DROP TABLE IF EXISTS lodging"
        self.base_controller.DeleteTable(query)

    def PostTableLodging(self, data):
        query = """INSERT INTO lodging (name, city, latitude, longitude, price, 
                    type, capacity, rooms_number, bathrooms_number, bedrooms_number, id_host) 
                    VALUES %s"""
        self.base_controller.PostTable(query, data)

    def PostOneElement(self,element):
        query=f"""
        Insert into lodging(name,city,latitude,longitude,
                            price,type,capacity,rooms_number,
                            bathrooms_number ,bedrooms_number,
                            id_host)
        values
        ('{element.name}', '{element.city}' ,'{element.latitude}','{element.longitude}',
        {element.price},'{element.type}',{element.capacity},{element.rooms_number},
        {element.bathrooms_number},{element.bedrooms_number},{element.id_host}
        );"""
        self.base_controller.PostTableOneElement(query=query)

class ControllerUser:
    def __init__(self):
        self.base_controller=BaseController()
    
    def CreateTableUser(self):
        query="""CREATE TABLE IF NOT EXISTS users(
                name varchar(50) not null,
                password varchar(50) not null
                );"""
        self.base_controller.CreateTable(query=query)
    
    def DeleteTableUser(self):
        query="""DROP TABLE IF EXISTS users"""
        self.base_controller.DeleteTable(query=query)
    
    def PostTableUser(self,element):
        query=f""" insert into users(name,password)
                    values
                    ('{element.name}','{element.password}');
        """
        self.base_controller.PostTableOneElement(query=query)

class ControllerReservation:
    def __init__(self):
        self.base_controller=BaseController()

    def CreateTableReservation(self):
        query="""CREATE TABLE IF NOT EXISTS reservation( 
            id_reservation SERIAL PRIMARY KEY,
            id_lodging INT NOT NULL,
            initial_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL
        );"""
        self.base_controller.CreateTable(query=query)
    
    def DeleteTableReservation(self): 
        query="""DROP TABLE IF EXISTS reservation"""
        self .base_controller.DeleteTable(query=query)
    
    def PostTableReservation(self,element):
        query=f""" insert into reservation(id_lodging,initial_date, end_date)
                    values({element.id_lodging},'{element.initial_date}','{(element.end_date)}'
                    );
        """
        self.base_controller.PostTableOneElement(query=query)

class ControllerImage:
    def __init__(self):
        self.base_controller=BaseController()
    
    def CreateTableImage(self):
        query=""" CREATE TABLE IF NOT EXISTS Image(
        id_image SERIAL PRIMARY KEY,
        lodging varchar(50) not null,
        address varchar(50) not null
        );
        """
        self.base_controller.CreateTable(query=query)

    def DeleteTableImage(self):
        query="""DROP TABLE IF EXISTS Image"""
        self.base_controller.DeleteTable(query=query)

    def postImage(self,element):
        query=f""" insert into Image(lodging,address)
        values('{element.lodging}','{element.lodging}');"""
        self.base_controller.PostTableOneElement(query=query)    

class Controllerhost:
    def __init__(self):
        self.base_controller=BaseController()
    
    def CreateTableHost(self):
        query="""CREATE TABLE IF NOT EXISTS host(
                host int not null
        );
        """
        self.base_controller.CreateTable(query=query)
    
    def DeleteTableHost(self):
        query="""DROP TABLE IF EXISTS host"""
        self.base_controller.DeleteTable(query=query)
    
    def posthost(self,element):
        query=f"""insert into host(host)
        values({element.host});"""
        self.base_controller.PostTableOneElement(query=query)





