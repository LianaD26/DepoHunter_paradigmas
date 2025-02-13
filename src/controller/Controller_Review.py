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
import controller.Controller_Result as contro_result

class ControllerReview:
    def __init__(self):
        self.base_controller=B_Controller.BaseController()
    
    def CreateTableReview(self):
        query="""CREATE TABLE IF NOT EXISTS review(
                id_review SERIAL PRIMARY KEY,
                user_name varchar(50) not null,
                id_lodging int not null,
                rating int not null,
                comment varchar(100) not null
                );"""
        self.base_controller.CreateTable(query=query)
    
    def PostTableUser(self, data):
        query = """INSERT INTO review ( id_review,user_name ,id_lodging, rating, comment) 
                    VALUES %s"""
        self.base_controller.PostTable(query, data)
    

    def PostTableUserOne(self,element):
        query=f""" insert into review( id_review, user_name ,id_lodging, rating, comment)
                    values
                    ({element.id_review}, '{element.user_name}',
                    {element.id_lodging},{element.rating},
                    '{element.comment}');
                """
        self.base_controller.PostTableOneElement(query=query)

#prueba_review=ControllerReview()
#prueba_review.CreateTableUser()
#prueba_review.PostTableUser(data="DepoHunter_paradigmas/src/utils/sample_reviews.csv")
#elemento_prueba=models.Review(id_review=90, user_name="pepito" ,id_lodging=2, rating=5, comment="beatiful")
#prueba_review.PostTableUserOne(element=elemento_prueba)



