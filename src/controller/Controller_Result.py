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


class ControllerResult():
    def __init__(self):
        self.base_controller = B_Controller.BaseController()
    
    def _execute_query(self, query, fetch_method="fetchall", params=None):
        cursor = self.base_controller.connection.cursor()
        cursor.execute(query, params or [])
        search = getattr(cursor, fetch_method)()  # Ajustado para que no se pase fetch_size
        cursor.close()
        return search
    
    def filterdefault(self):
        query = """ SELECT l.name, l.city, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                """
        search = self._execute_query(query)
        
        if search is not None: 
            return search
        else: 
            return None    
    
    def FilterCityDate(self, city, initial_date, end_date):
        query = """ SELECT l.name, l.city, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.city = %s OR r.initial_date = %s OR r.end_date = %s """
        search = self._execute_query(query, params=(city, initial_date, end_date))
        
        if search is not None:    
            return search
        else:
            return None
    
    def Filterprice(self, price):
        query = """ SELECT l.name, l.city, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.price = %s """
        search = self._execute_query(query, params=(price,))
        
        if search is not None: 
            return search
        else:
            return None
    
    def filtertype(self, type):
        query = """ SELECT l.name, l.city, l.price, 
                    l.type, l.capacity, l.rooms_number, 
                    l.bathrooms_number, l.bedrooms_number, r.initial_date, r.end_date
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    WHERE l.type = %s """
        search = self._execute_query(query, params=(type,))
        
        if search is not None: 
            return search
        else:
            return None
    
    def filterUser(self, name):
        query = """ SELECT * FROM users WHERE name=%s """
        search = self._execute_query(query, fetch_method="fetchone", params=(name,))
        
        if search is not None: 
            return search
        else: 
            return None


# Ejemplo de uso
#elementobusqueda = ControllerResult()
#print(elementobusqueda.filterdefault())
#print(elementobusqueda.FilterCityDate(city="Madrid", initial_date="2025-12-02", end_date="2025-12-02"))
#print(elementobusqueda.Filterprice(price=150))
#print(elementobusqueda.filtertype(type="Casa"))
