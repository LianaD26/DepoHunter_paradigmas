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
    
    def _execute_query(self, query, fetch_method="fetchall"):
        cursor = self.base_controller.connection.cursor()
        cursor.execute(query)
        
        if fetch_method == "fetchone":
            search = cursor.fetchone()
        else:
            search = cursor.fetchall()

        cursor.close()
        return search
    
    def filterdefault(self):
        query = """select  l.id ,l.name,l.city, l.price,
                l.type, l.capacity, l.rooms_number
                ,l.bathrooms_number, l.bedrooms_number,
                h.host_name,i.addressone,i.addresstwo,i.addresstree
                from lodging l

                LEFT JOIN host h ON l.id = h.id_lodging
                LEFT JOIN image i ON l.id = i.id_lodging;
                """
        return self._execute_query(query)
    
    def FilterCityDate(self, city, initial_date, end_date):
        query = f"""SELECT 
                    l.id,l.name, l.city, l.price,
                    l.type, l.capacity, l.rooms_number,
                    l.bathrooms_number, l.bedrooms_number,
                    h.host_name, i.addressone, i.addresstwo, i.addresstree
                    FROM lodging l
                    LEFT JOIN reservation r ON l.id = r.id_lodging
                    LEFT JOIN host h ON l.id = h.id_lodging
                    LEFT JOIN image i ON l.id = i.id_lodging
                    WHERE l.city = '{city}'  AND r.initial_date= '{initial_date}' AND r.end_date = '{end_date}';
                    """
        return self._execute_query(query)
    
    def Filterprice(self, price):
        query = f""" select  l.id,l.name,l.city, l.price,
                    l.type, l.capacity, l.rooms_number
                    ,l.bathrooms_number, l.bedrooms_number,
                    h.host_name,i.addressone,i.addresstwo,i.addresstree
                    from lodging l

                    LEFT JOIN host h ON l.id = h.id_lodging
                    LEFT JOIN image i ON l.id = i.id_lodging
                    WHERE l.price = {price} """
        return self._execute_query(query)
    
    def filtertype(self, type):
        query = f""" 
            select  l.id, l.name,l.city, l.price,
                    l.type, l.capacity, l.rooms_number
                    ,l.bathrooms_number, l.bedrooms_number,
                    h.host_name,i.addressone,i.addresstwo,i.addresstree
                    from lodging l

                    LEFT JOIN host h ON l.id = h.id_lodging
                    LEFT JOIN image i ON l.id = i.id_lodging
            WHERE l.type = '{type}' """
        return self._execute_query(query)
    
    def filterUser(self, name):
        query = f""" SELECT * FROM users 
                    WHERE name = '{name}'"""
        return self._execute_query(query, fetch_method="fetchone")

    def filter_Review(self,id_lodging):
        query = f""" SELECT * FROM  review 
                    WHERE id_lodging = '{id_lodging}'"""
        return self._execute_query(query)



# Ejemplo de uso
#elementobusqueda = ControllerResult()
#print(elementobusqueda.filterdefault())
#print(elementobusqueda.FilterCityDate(city="Madrid", initial_date="2025-12-02", end_date="2025-12-02"))
#print(elementobusqueda.Filterprice(price=150))
#print(elementobusqueda.filtertype(type="Casa"))
#print(elementobusqueda.filter_Review(id_lodging=2))
