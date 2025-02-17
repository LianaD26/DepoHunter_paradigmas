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

class ControllerImage:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
    def CreateTableImage(self):
        query=""" CREATE TABLE IF NOT EXISTS Image(
        id_image SERIAL PRIMARY KEY,
        id_lodging int not null,
        addressone varchar(200) not null,
        addresstwo varchar(200) not null,
        addresstree varchar(200) not null
        );
        """
        self.base_controller.CreateTable(query=query)
    
    def PostDataImage(self,data):
        query = """INSERT INTO Image (id_image,id_lodging,
                    addressone,addresstwo,addresstree) 
                    VALUES %s
                    """
        self.base_controller.PostTable(query, data,table_name="Image")

#imagen_ejemplo=ControllerImage()
#imagen_ejemplo.CreateTableImage()
#imagen_ejemplo.PostDataImage(data="DepoHunter_paradigmas/src/utils/urls.csv")

