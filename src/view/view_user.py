from flask import Blueprint, render_template
import sys
import os
sys.path.append("src")
sys.path.append("DepoHunter_paradigmas/src")
import controller.Controller_host as Controller_host
import controller.Controller_Image as Controller_Image
import controller.Controller_Lodging as  Controller_Lodging
import controller.Controller_Reservation as Controller_Reservation
import controller.Controller_Result as Controller_Result
import controller.Controller_user as Controller_user
import controller.Controller_Review as  Controller_Review

instance_controller_host=Controller_host.Controllerhost()
instance_controller_Image=Controller_Image.ControllerImage()
instance_controller_Lodging=Controller_Lodging.ControllerLodging()
instance_controller_Reservation=Controller_Reservation.ControllerReservation()
instance_controller_Result=Controller_Result.ControllerResult()
instance_controller_user=Controller_user.ControllerUser()
instance_controller_Review=Controller_Review.ControllerReview()

instance_controller_host.CreateTableHost()
instance_controller_Image.CreateTableImage()
instance_controller_Lodging.CreateTableLodging()
instance_controller_Reservation.CreateTableReservation()
instance_controller_user.CreateTableUser()
instance_controller_Review.CreateTableReview()


blueprint = Blueprint( "view_user", __name__, template_folder="templates" )

alojamientos = [
   {"id": 100, "nombre": "Alojamiento1", "precio": 123000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg"},
   {"id": 101, "nombre": "Alojamiento2", "precio": 150000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg"},
   {"id": 102, "nombre": "Alojamiento3", "precio": 95000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg"}
]
@blueprint.route("/")
def home():
   return render_template("home.html", alojamientos=alojamientos)

@blueprint.route("/alojamiento/<int:id>")
def alojamiento_detalle(id):
    alojamiento = next((a for a in alojamientos if a["id"] == id), None)
    if alojamiento is None:
        return "Alojamiento no encontrado", 404
    return render_template("detail.html", alojamiento=alojamiento)

@blueprint.route('/pago')
def pago():
    return render_template('pago.html')

@blueprint.route("/Login")
def Login():
   return render_template("login.html")

@blueprint.route("/Register")
def Register():
   return render_template("register.html")