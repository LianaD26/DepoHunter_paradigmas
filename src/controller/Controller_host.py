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


class Controllerhost:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
    def CreateTableHost(self):
        query="""CREATE TABLE IF NOT EXISTS host(
                host_name int not null,
                id_lodging int not null
        );
        """
        self.base_controller.CreateTable(query=query)
    
    def PostDataHost(self,data):
        query = """INSERT INTO lodging (host_name,id_lodging) 
                    VALUES %s"""
        self.base_controller.PostTable(query, data)


#ejemplofun=Controllerhost()
#ejemplofun.CreateTableHost()
#ejemplofun.PostDataHost(data="")
