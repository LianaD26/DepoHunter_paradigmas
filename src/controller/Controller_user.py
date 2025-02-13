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

#achu
#import model.models_table as models
#achu

class ControllerUser:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
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
        try:     
            models.User.checkregister(consult=element)
            query=f""" insert into users(name,password)
                        values
                        ('{element.name}','{element.password}');
                    """
            self.base_controller.PostTableOneElement(query=query)
        
        except models.user_repeact as error_user_repeact:
            print(error_user_repeact)
        


user_ejemplo=ControllerUser()
#user_ejemplo.CreateTableUser()
user_element=models.User(name="David",password="123456")
user_ejemplo.PostTableUser(element=user_element)
#user_ejemplo.DeleteTableUser()
