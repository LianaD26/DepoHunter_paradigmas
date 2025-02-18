from flask import Blueprint, render_template,  request, redirect, url_for, flash, request, session
import sys
sys.path.append("src")
import controller.Controller_host as Controller_host
import controller.Controller_Image as Controller_Image
import controller.Controller_Lodging as  Controller_Lodging
import controller.Controller_Reservation as Controller_Reservation
import controller.Controller_Result as Controller_Result
import controller.Controller_user as Controller_user
import controller.Controller_Review as  Controller_Review
import model.model_tables as models
from model.model_tables import User
from datetime import datetime

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

instance_controller_host.PostDataHost(data="src/utils/host_data.csv")
instance_controller_Image.PostDataImage(data="src/utils/urls.csv")
instance_controller_Lodging.PostDataLodging(data="src/utils/df_lodging.csv")
instance_controller_Review.PostDataReview(data="src/utils/sample_reviews.csv")


blueprint = Blueprint( "view_user", __name__, template_folder="templates" )

@blueprint.route("/")
def home():
   alojamientos=instance_controller_Result.filterdefault()
   return render_template("home.html", alojamientos=alojamientos)


@blueprint.route("/alojamiento/<int:id>", methods=["GET", "POST"])
def alojamiento_detalle(id):
    if request.method == "POST":
        comentario = request.form.get("comentario-post") 
        calificacion = request.form.get("calificacion")
        user_name=session.get("username")
        if user_name!=None:
            element_comment=models.Review(id_review=None, user_name= user_name ,id_lodging=id, rating=int(calificacion), comment=comentario)
            instance_controller_Review.PostTableUserOne(element=element_comment)
        else: 
            return redirect(url_for('view_user.login'))

    comment = instance_controller_Result.filter_Review(id_lodging=id)
    alojamientos = instance_controller_Result.filterdefault()

    alojamiento = next((a for a in alojamientos if a["id"] == id), None)
    if alojamiento is None:
        return "Alojamiento no encontrado", 404
    averange = models.Review.calculate_Start(comment)

    return render_template("detail.html", alojamiento=alojamiento, comments=comment, averange=averange)

@blueprint.route('/alojamiento/<int:id>/pago', methods=['POST'])
def pago(id):
    try:
        initial_date = request.form.get("fecha_inicio")
        end_date = request.form.get("fecha_fin")
        
        return render_template('pago.html', id=id, initial_date=initial_date, end_date=end_date)
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.alojamiento_detalle", id=id))

@blueprint.route('/alojamiento/<int:id>/confirmar_pago', methods=['POST'])
def confirmar_pago(id):
    try:
        initial_date = request.form.get("initial_date")
        end_date = request.form.get("end_date")
        banco = request.form.get("banco")
        tarjeta = request.form.get("tarjeta")
        cvv = request.form.get("cvv")
        
        initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Lógica para guardar la reserva en la base de datos
        reservation = models.Reservation(id_reservation=None, id_lodging=id, initial_date=initial_date, end_date=end_date)
        instance_controller_Reservation.PostTableReservation(reservation)
        
        flash("Reserva realizada con éxito.", "success")
        return redirect(url_for("view_user.alojamiento_detalle", id=id))
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.alojamiento_detalle", id=id))



@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username: #aca se puede realizar validaciones 
            session["username"] = username
            return redirect(url_for("view_user.home"))  # Corrección de la redirección
    return render_template("login.html")

@blueprint.route("/logout") #enviandolo a esta ruta elimina al usuario
def logout():
    session.pop("username", None)  # Eliminamos el usuario de la sesión
    return redirect(url_for("view_user.home"))  # Redirigir al login

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


@blueprint.route("/reservations")
def reservations():
    try:
        # Obtener las reservas en proceso y finalizadas del controlador
        reservas_proceso = instance_controller_Result.filter_reservas_proceso()  # Implementa esta función
        reservas_finalizadas = instance_controller_Result.filter_reservas_finalizadas()  # Implementa esta función
        
        return render_template("reservations.html", reservas_proceso=reservas_proceso, reservas_finalizadas=reservas_finalizadas)
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.home"))


@blueprint.route('/reservations/<int:reserva_id>', methods=['POST'])
def cancel_reservation(reserva_id):
    try:
        # Llamar la función que cancela la reserva en la base de datos
        instance_controller_Reservation.CancelReservation(reserva_id)
        
        # Mensaje de éxito
        flash("Reserva cancelada con éxito.", "success")
        
        # Redirigir a la vista de reservas del usuario
        return redirect(url_for("view_user.reservations"))
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.reservations"))


@blueprint.route("/lodgings", methods=["GET", "POST"])
def main_filter_lodgings():
    # Obtener los valores del formulario
    city = request.form.get("city")
    initial_date = request.form.get("initial_date")
    end_date = request.form.get("end_date")

    # Llamar la función que filtra los alojamientos
    new_lodgings = instance_controller_Result.FilterCityDate(city, initial_date, end_date)

    return render_template("home.html", alojamientos=new_lodgings)

@blueprint.route('/filters', methods=["GET", "POST"])
def filters_lodgings():
    # Obtener el tipo
    tipo = request.form.get("tipo_")
    # Obtener el precio max
    precio_max = request.form.get("precio_max")
    if tipo and precio_max:
        precio_max = int(precio_max)
        #filtro de las dos cosas
        new_lodgings = instance_controller_Result.filterTypePrice(tipo, precio_max)
    elif tipo:
        new_lodgings = instance_controller_Result.filtertype(tipo)
    elif precio_max:
        precio_max = int(precio_max)
        new_lodgings = instance_controller_Result.Filterprice(precio_max)
    return render_template('home.html', alojamientos=new_lodgings)
@blueprint.route("/alojamiento/<int:id>/reservar", methods=["POST"])
def make_reservation(id):
    try:
        initial_date = request.form.get("fecha_inicio")
        end_date = request.form.get("fecha_fin")
        
        initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        reservation = models.Reservation(id_reservation=None, id_lodging=id, initial_date=initial_date, end_date=end_date)
        
        # Save reservation in the DB
        instance_controller_Reservation.PostTableReservation(reservation)
        
        flash("Reserva realizada con éxito.", "success")
        return redirect(url_for("view_user.alojamiento_detalle", id=id))
    
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for("view_user.alojamiento_detalle", id=id))
