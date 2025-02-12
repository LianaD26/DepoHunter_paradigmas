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

class ControllerImage:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
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

#imagen_ejemeplo=ControllerImage()
#imagen_ejemeplo.CreateTableImage()
#imagen_element=models.image(id_image=None,lodging="123",address="453")
#imagen_ejemeplo.postImage(element=imagen_element)
#imagen_ejemeplo.DeleteTableImage()
