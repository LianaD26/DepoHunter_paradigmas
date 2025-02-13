from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("DepoHunter_paradigmas/src")
import config.SecretConfig as secretconfig
import model.model_tables as models
import utils.logic_controllerresult as logic_cont
import controller.Base_Controller as B_Controller

class ControllerLodging:
    def __init__(self):
        self.base_controller = B_Controller.BaseController()

    def CreateTableLodging(self): #revisar porque el type puede generar conflicto
        
        query = """
                CREATE TYPE lodging_type AS ENUM (
                    'Apartamento',
                    'Casa',
                    'Casa de huéspedes');

                CREATE TABLE IF NOT EXISTS lodging (
                    id serial PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    city varchar(50) NOT NULL,
                    price int NOT NULL,
                    type lodging_type NOT NULL,  
                    capacity int NOT NULL,
                    rooms_number int NOT NULL,
                    bathrooms_number int NOT NULL,
                    bedrooms_number int NOT NULL,
                    id_host int NOT NULL
                );
                """
        self.base_controller.CreateTable(query)

    
    def DeleteTableLodging(self):
        query = "DROP TABLE IF EXISTS lodging"
        self.base_controller.DeleteTable(query)

    
    def PostTableLodging(self, data):
        query = """INSERT INTO lodging (name, city, price, 
                    type, capacity, rooms_number, bathrooms_number, bedrooms_number, id_host) 
                    VALUES %s"""
        self.base_controller.PostTable(query, data)


#lodging_ejemplo=ControllerLodging()
#lodging_ejemplo.CreateTableLodging()
#lodging_ejemplo.PostTableLodging(data="DepoHunter_paradigmas/src/utils/df_lodging.csv")
#lodging_element=models.Lodging(name="d"
#                ,city="d",latitude="3",
#                longitude="2",price=2,
#                type="Casa",capacity=2,
#                rooms_number=32,bathrooms_number=32,
#                bedrooms_number=32,id_host=3)
#lodging_ejemplo.PostOneElement(element=lodging_element)
