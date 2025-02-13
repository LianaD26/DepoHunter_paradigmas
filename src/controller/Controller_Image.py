from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("DepoHunter_paradigmas/src")
import config.SecretConfig as secretconfig
import model.model_tables as models
import controller.Base_Controller as B_Controller

class ControllerImage:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
    def CreateTableImage(self):
        query=""" CREATE TABLE IF NOT EXISTS Image(
        id_image SERIAL PRIMARY KEY,
        id_lodging varchar(50) not null,
        addressone varchar(50) not null,
        addresstwo varchar(50) not null,
        addresstree varchar(50) not null
        );
        """
        self.base_controller.CreateTable(query=query)

#imagen_ejemeplo=ControllerImage()
#imagen_ejemeplo.CreateTableImage()
#imagen_element=models.image(id_image=None,lodging="123",address="453")
#imagen_ejemeplo.postImage(element=imagen_element)
#imagen_ejemeplo.DeleteTableImage()
