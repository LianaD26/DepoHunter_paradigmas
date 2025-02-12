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


class ControllerReservation:
    def __init__(self):
        self.base_controller= B_Controller.BaseController()

    def CreateTableReservation(self):
        query="""CREATE TABLE IF NOT EXISTS reservation( 
            id_reservation SERIAL PRIMARY KEY,
            id_lodging INT NOT NULL,
            initial_date DATE NOT NULL,
            end_date DATE NOT NULL
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

#reservation_ejemeplo=ControllerReservation()
#reservation_ejemeplo.CreateTableReservation()
#reservation_element=models.reservation(id_reservation=None,id_lodging=123,initial_date="12-02-2025",end_date= "8-02-2025")
#reservation_ejemeplo.PostTableReservation(reservation_element)
#reservation_ejemeplo.DeleteTableReservation()
