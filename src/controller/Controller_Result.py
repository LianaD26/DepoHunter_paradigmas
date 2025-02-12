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


class ControllerResult():
    def __init__(self):
        self.base_controller = B_Controller.BaseController()
    
    def _execute_query(self, query, fetch_method="fetchmany", fetch_size=10):
        cursor = self.base_controller.connection.cursor()
        cursor.execute(query)
        search = getattr(cursor, fetch_method)(fetch_size) if fetch_method == "fetchmany" else cursor.fetchone()
        cursor.close()
        return search
    
    def filterdefault(self):
        query = """ SELECT l.name, l.city, l.latitude, l.longitude, l.price, 
                l.type, l.capacity, l.rooms_number, 
                l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                FROM lodging l
                LEFT JOIN reservation r ON l.id = r.id_lodging
                """
        search = self._execute_query(query)
        return logic_cont.ManipulateData(search)
    
    def FilterCityDate(self, city, initial_date, end_date):
        query = f""" SELECT l.name, l.city, l.latitude, l.longitude, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.city = '{city}' OR r.initial_date = '{initial_date}' OR r.end_date = '{end_date}' """
        search = self._execute_query(query)
        return logic_cont.ManipulateData(search)
    
    def Filterprice(self, price):
        query = f""" SELECT l.name, l.city, l.latitude, l.longitude, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.price = {price} """
        search = self._execute_query(query)
        return logic_cont.ManipulateData(search)
    
    def filtertype(self, type):
        query = f""" SELECT l.name, l.city, l.latitude, l.longitude, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.type = '{type}' """
        search = self._execute_query(query)
        return logic_cont.ManipulateData(search)
    
    def filterUser(self, name):
        query = f""" SELECT * FROM users WHERE name='{name}' """
        search = self._execute_query(query, fetch_method="fetchone")
        return models.user(name=search[0], password=search[1])


#elementobusqueda=ControllerResult()
#elementobusqueda.filterdefault()
#elementobusqueda.FilterCityDate(city="Madrid", initial_date="2025-12-02", end_date="2025-12-02")
#elementobusqueda.Filterprice(price=150)
#elementobusqueda.filtertype(type="Casa")
