from flask import Blueprint, render_template,  request, redirect, url_for, flash, request
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
from model.model_tables import User

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
    comment=instance_controller_Result.filter_Review(id_lodging=id)
    alojamientos=instance_controller_Result.filterdefault()
    
    alojamiento = next((a for a in alojamientos if a["id"] == id), None)
    if alojamiento is None:
        return "Alojamiento no encontrado", 404
    
    return render_template("detail.html", alojamiento=alojamiento,comments=comment)

@blueprint.route('/pago')
def pago():
   return render_template('pago.html')


@blueprint.route("/login")
def login():
   return render_template("login.html")

@blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            name = request.form.get("name")
            password = request.form.get("password")
            password_verification = request.form.get("password_verification")

            if password != password_verification:
                flash("Las contraseñas no coinciden.", "error")
                return redirect(url_for("view_user.register"))
            
            user_check = instance_controller_Result.filterUser(name)
            if user_check:
                flash("El nombre de usuario ya está registrado.", "error")
                return redirect(url_for("view_user.register"))

            user = User(name, password)
            user.validate_user()
            instance_controller_user.PostTableUser(user)
            flash("Usuario registrado con éxito.", "success")
            return redirect(url_for("view_user.login"))

        return render_template("register.html")
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.register"))



# datos de prueba para los estados reservado y finalizado
reservas_proceso = [{'id':1, 'alojamiento':"uno", 'fecha_inicio':'26/11/2004', 'fecha_fin':'30/11/2004'}, {'id':2, 'alojamiento':"dos", 'fecha_inicio':'26/11/2004', 'fecha_fin':'30/11/2004'}]
reservas_finalizadas = [{'id':3, 'alojamiento':"tres", 'fecha_inicio':'26/11/2004', 'fecha_fin':'30/11/2004'}, {'id':4, 'alojamiento':"cuatro", 'fecha_inicio':'26/11/2004', 'fecha_fin':'30/11/2004'}]

@blueprint.route("/reservations")
def reservations():
   
   return render_template("reservations.html", reservas_proceso= reservas_proceso, reservas_finalizadas=reservas_finalizadas)

@blueprint.route('/reservations/<int:reserva_id>', methods=['POST'])
def cancel_reservation(reserva_id):
   # Llamar la función que cancela la reserva en la base de datos
   #cancelar_reserva(reserva_id)  # Implementa esta función en tu backend

   # Mensaje de éxito (opcional)

   # Redirigir a la vista de reservas del usuario

   return render_template("reservations.html", reservas_proceso= reservas_proceso, reservas_finalizadas=reservas_finalizadas)

@blueprint.route("/lodgings", methods=["GET", "POST"])
def main_filter_lodgings():
    # Obtener los valores del formulario
    city = request.form.get("city")
    initial_date = request.form.get("initial_date")
    end_date = request.form.get("end_date")

    # Llamar la función que filtra los alojamientos
    new_lodgings = instance_controller_Result.FilterCityDate(city, initial_date, end_date)

    return render_template("home.html", alojamientos=new_lodgings)