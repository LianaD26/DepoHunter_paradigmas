from flask import Blueprint, render_template
import sys
import os
sys.path.append("src")
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

instance_controller_host.PostDataHost(data="src/utils/host_data.csv")
instance_controller_Image.PostDataImage(data="src/utils/urls.csv")
instance_controller_Lodging.PostDataLodging(data="src/utils/df_lodging.csv")
instance_controller_Review.PostDataReview(data="src/utils/sample_reviews.csv")


blueprint = Blueprint( "view_user", __name__, template_folder="templates" )

@blueprint.route("/")
def home():
   alojamientos=instance_controller_Result.filterdefault()
   return render_template("home.html", alojamientos=alojamientos)


@blueprint.route("/alojamiento/<int:id>")
def alojamiento_detalle(id):
    alojamientos=instance_controller_Result.filterdefault()
    alojamiento = next((a for a in alojamientos if a["id"] == id), None)
    if alojamiento is None:
        return "Alojamiento no encontrado", 404
    return render_template("detail.html", alojamiento=alojamiento)


@blueprint.route('/pago')
def pago():
   return render_template('pago.html')


@blueprint.route("/login")
def login():
   return render_template("login.html")

@blueprint.route("/register")
def register():
   return render_template("register.html")

@blueprint.route("/reservations")
def reservations():
   return render_template("reservations.html")