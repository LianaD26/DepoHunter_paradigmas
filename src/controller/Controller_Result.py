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

general_keys=[ "id" ,"name","city", "price", "type", "capacity", "rooms_number",
            "bathrooms_number", "bedrooms_number", "host_name","addressone",
            "addresstwo","addresstree"]

user_key=["name","password"]

Review_key=["id_review","user_name","id_lodging","rating", "comment"]

def dic_get(tuple,list_keys):
    list_result_element=[]
    keys=list_keys
    for element in tuple:
        list_result_element.append(dict(zip(keys,element)))  
    return list_result_element



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
        query_result=self._execute_query(query)
        return dic_get(tuple=query_result,list_keys=general_keys)
    
    
    def FilterCityDate(self, city, initial_date, end_date):
        query =f""" SELECT 
                l.id, l.name, l.city, l.price,
                l.type, l.capacity, l.rooms_number,
                l.bathrooms_number, l.bedrooms_number,
                h.host_name, i.addressone, i.addresstwo, i.addresstree
                FROM lodging l
                LEFT JOIN reservation r ON l.id = r.id_lodging
                LEFT JOIN host h ON l.id = h.id_lodging
                LEFT JOIN image i ON l.id = i.id_lodging
                WHERE l.city = '{city}' AND '{initial_date}' > CURRENT_DATE   
                AND (  COALESCE(r.end_date, '0001-01-01') <= '{initial_date}'  
                OR COALESCE(r.initial_date, '9999-12-31') >= '{end_date}' );
    """
        query_result = self._execute_query(query)
        return dic_get(tuple=query_result, list_keys=general_keys)
    
    
    def Filterprice(self, price):
        query = f""" select  l.id,l.name,l.city, l.price,
                    l.type, l.capacity, l.rooms_number
                    ,l.bathrooms_number, l.bedrooms_number,
                    h.host_name,i.addressone,i.addresstwo,i.addresstree
                    from lodging l

                    LEFT JOIN host h ON l.id = h.id_lodging
                    LEFT JOIN image i ON l.id = i.id_lodging
                    WHERE l.price <= {price} """
        query_result=self._execute_query(query)
        return dic_get(tuple=query_result,list_keys=general_keys)
    
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
        query_result=self._execute_query(query)
        return dic_get(tuple=query_result,list_keys=general_keys)
    
    def filterTypePrice(self, type_, price): 
        query = f""" 
            SELECT  l.id, l.name, l.city, l.price,
                    l.type, l.capacity, l.rooms_number,
                    l.bathrooms_number, l.bedrooms_number,
                    h.host_name, i.addressone, i.addresstwo, i.addresstree
                    FROM lodging l
                    LEFT JOIN host h ON l.id = h.id_lodging
                    LEFT JOIN image i ON l.id = i.id_lodging
            WHERE l.price <={price} and l.type = '{type_}'"""

        query_result = self._execute_query(query)
        return dic_get(tuple=query_result, list_keys=general_keys)
        
    def filterUser(self, name):
        query = f""" SELECT * FROM users 
                    WHERE name = '{name}'"""
        query_result = self._execute_query(query, fetch_method="fetchone")
        return query_result 

    
    def filter_Review(self,id_lodging):
        query = f""" SELECT * FROM  review 
                    WHERE id_lodging = '{id_lodging}'"""
        query_result=self._execute_query(query)
        return dic_get(tuple=query_result,list_keys=Review_key)
    
    def filter_reservas_proceso(self):
        query = """
        SELECT id_reservation, id_lodging, initial_date, end_date 
        FROM reservation
        WHERE end_date >= CURRENT_DATE;
        """
        result = self.base_controller.ExecuteQuery(query=query)
        reservas_proceso = [{"id": row[0], "alojamiento": row[1], "fecha_inicio": row[2], "fecha_fin": row[3]} for row in result]
        return reservas_proceso

    def filter_reservas_finalizadas(self):
        query = """
        SELECT id_reservation, id_lodging, initial_date, end_date 
        FROM reservation
        WHERE end_date < CURRENT_DATE;
        """
        result = self.base_controller.ExecuteQuery(query=query)
        reservas_finalizadas = [{"id": row[0], "alojamiento": row[1], "fecha_inicio": row[2], "fecha_fin": row[3]} for row in result]
        return reservas_finalizadas



# Ejemplo de uso
elementobusqueda = ControllerResult()
#print(elementobusqueda.filterTypePrice(type_="Apartamento",price=200))
#print(elementobusqueda.filterdefault())
#print(elementobusqueda.FilterCityDate(city="Bogotá", initial_date="2026-12-02", end_date="2029-12-02"))
#print(elementobusqueda.Filterprice(price=0))
#print(elementobusqueda.filtertype(type="Casa"))
#print(elementobusqueda.filter_Review(id_lodging=2))
