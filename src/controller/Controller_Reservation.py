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
from src.controller.Controller_Result import ControllerResult


class ControllerReservation:
    def __init__(self):
        self.base_controller = B_Controller.BaseController()
        self.Controller_Result = ControllerResult()

    def CreateTableReservation(self):
        query = """
        CREATE TABLE IF NOT EXISTS reservation (
            id_reservation SERIAL PRIMARY KEY,
            id_lodging INT NOT NULL,
            initial_date DATE NOT NULL,
            end_date DATE NOT NULL,
            name VARCHAR(50) NOT NULL,
            FOREIGN KEY (id_lodging) REFERENCES lodging(id) ON DELETE CASCADE,
            FOREIGN KEY (name) REFERENCES users(name) ON DELETE CASCADE
        );
        """
        self.base_controller.PostTableOneElement(query=query)


    def PostTableReservation(self, element):
        query = """
        INSERT INTO reservation (id_lodging, initial_date, end_date, name)
        VALUES (%s, %s, %s, %s);
        """ % (element.id_lodging, f"'{element.initial_date}'", f"'{element.end_date}'", f"'{element.name}'")

        try:
            self.base_controller.PostTableOneElement(query=query)
            print("✅ Reserva guardada con éxito.")
        except Exception as e:
            print(f"❌ Error al guardar la reserva: {e}")

    def CancelReservation(self, reserva_id):
        query = "DELETE FROM reservation WHERE id_reservation = %s;"
        try:
            self.Controller_Result._execute_query(query, (reserva_id,))  # ✅ Pasar los parámetros correctamente
            print(f"✅ Reserva {reserva_id} cancelada exitosamente.")
        except Exception as e:
            print(f"❌ Error cancelando la reserva: {e}")

    
    

#reservation_ejemeplo=ControllerReservation()
#reservation_ejemeplo.CreateTableReservation()
#reservation_element=models.Reservation(id_reservation=None,id_lodging=123,initial_date="2025-12-02",end_date= "2025-8-02")
#reservation_ejemeplo.PostTableReservation(reservation_element)
#reservation_ejemeplo.DeleteTableReservation()
