from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("src")
import config.SecretConfig as secretconfig
import model.model_tables as models
import controller.Base_Controller as B_Controller

class ControllerLodging:
    def __init__(self):
        self.base_controller = B_Controller.BaseController()

    def CreateTableLodging(self): #revisar porque el type puede generar conflicto
        
        query = """

                CREATE TABLE IF NOT EXISTS lodging (
                    id serial PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    city varchar(50) NOT NULL,
                    price int NOT NULL,
                    type varchar(50) NOT NULL,  
                    capacity int NOT NULL,
                    rooms_number int NOT NULL,
                    bathrooms_number int NOT NULL,
                    bedrooms_number int NOT NULL
                );
                """
        self.base_controller.CreateTable(query)

    
    def PostDataLodging(self, data):
        query = """INSERT INTO lodging (name, city, price, 
                    type, capacity, rooms_number, bathrooms_number, bedrooms_number) 
                    VALUES %s
                    """
        self.base_controller.PostTable(query, data,table_name="lodging")




#lodging_ejemplo=ControllerLodging()
#lodging_ejemplo.CreateTableLodging()
#lodging_ejemplo.PostTableLodging(data="DepoHunter_paradigmas/src/utils/df_lodging.csv")
