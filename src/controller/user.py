import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("DepoHunter_paradigmas/src")
import controller.SecretConfig as secretconfig


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

    def PostTable(self, query: str, data: str) -> None:
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


class ControllerUser:
    def __init__(self):
        self.base_controller=BaseController()
    
    def CreateTableUser(self):
        query=""" CREATE TABLE IF NOT EXISTS user(
                name varchart(50) not null,
                password varchar(50) not null
                );"""
        self.base_controller.CreateTable(query=query)
    
    def DeleteTableUser(self):
        query="""DROP TABLE IF EXISTS user"""
        self.base_controller.DeleteTable(query=query)
    
    def PostTableUser():
        pass


class ControllerReservation:
    def __init__(self):
        self.base_controller=BaseController()

    def CreateTableReservation(self):
        query="""CREATE TABLE IF NOT EXISTS reservation( 
            id_reservation SERIAL PRIMARY KEY,
            id_lodging INT NOT NULL,
            initial_date TIMESTAMP NOT NULL,
            end_date TIMESTAMP NOT NULL,
        );     
        """
        self.base_controller.CreateTable(query=query)
    
    def DeleteTableReservation(self): 
        query="""DROP TABLE IF EXISTS reservation"""
        self .base_controller.DeleteTable(query=query)
    
    def PostTableReservation(self):
        pass

class ControllerImage:
    def __init__(self):
        self.base_controller=BaseController()
    
    def CreateTableImage(self):
        query=""" CREATE TABLE IF NOT EXISTS Image(
        id_imagen SERIAL PRIMARY KEY,
        lodging varchar(50) not null,
        address varchar(50) not null
        );
        """
        self.base_controller.CreateTable(query=query)

    def DeleteTableImage(self):
        query="""DROP TABLE IF EXISTS Image"""
        self.base_controller.DeleteTable(query=query)    


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

    






