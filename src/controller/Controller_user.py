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
import controller.Controller_Result as contro_result


class ControllerUser:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
    def CreateTableUser(self):
        query="""CREATE TABLE IF NOT EXISTS users(
                name varchar(50) not null,
                password varchar(50) not null
                );"""
        self.base_controller.CreateTable(query=query)
    
    
    def PostTableUser(self,element):
        try:     
            elementobusqueda=contro_result.ControllerResult()

            models.User.checkregister(consult=elementobusqueda.filterUser(element.name))
            query=f""" insert into users(name,password)
                        values
                        ('{element.name}','{element.password}');
                    """
            self.base_controller.PostTableOneElement(query=query)
        
        except models.user_repeact as error_user_repeact:
            print(error_user_repeact)
        


#user_ejemplo=ControllerUser()
#user_ejemplo.CreateTableUser()
#user_element=models.User(name="PEPE",password="123456")
#user_ejemplo.PostTableUser(element=user_element)
#user_ejemplo.DeleteTableUser()