from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values
import sys
import os
import pandas as pd
sys.path.append("src")
import config.SecretConfig as secretconfig
import model.model_tables as models

class BaseController:
    def __init__(self):
        self.connection = self._GetConnection()
    
    def _GetConnection(self):
        return psycopg2.connect(
            dbname=secretconfig.PGDATABASE,
            user=secretconfig.PGUSER,
            password=secretconfig.PGPASSWORD,
            host=secretconfig.PGHOST,
            port=secretconfig.PGPORT
        )
    
    def CreateTable(self, query):
        cursor_lodging = self.connection.cursor()
        cursor_lodging.execute(query)
        self.connection.commit()
        cursor_lodging.close()
    
    def DeleteTable(self, query):
        cursor_lodging = self.connection.cursor()
        cursor_lodging.execute(query)
        self.connection.commit()
        cursor_lodging.close()
    
    def PostTable(self,query, data,table_name):
        data_frame = pd.read_csv(data)
        cursor_lodging = self.connection.cursor()
        cursor_lodging.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor_lodging.fetchone()[0]
        if count == 0:
            data_tuples = list(data_frame.itertuples(index=False, name=None))
            execute_values(cursor_lodging, query, data_tuples)
            self.connection.commit()
        cursor_lodging.close()
    
    def PostTableOneElement(self, query):
        cursor_lodging = self.connection.cursor()
        cursor_lodging.execute(query)
        self.connection.commit()
        cursor_lodging.close()