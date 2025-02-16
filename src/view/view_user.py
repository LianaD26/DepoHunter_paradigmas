from flask import Blueprint, render_template

blueprint = Blueprint( "view_user", __name__, template_folder="templates" )

alojamientos = [
   {"id": 100, "nombre": "Alojamiento1", "precio": 123000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg", "ubicacion":"Guarne Antioquia"},
   {"id": 101, "nombre": "Alojamiento2", "precio": 150000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg", "ubicacion":"Cartagena Bolivar"},
   {"id": 102, "nombre": "Alojamiento3", "precio": 95000, "imagen1": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg", "imagen2":"https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg", "imagen3" : "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg", "ubicacion":"Bogota Colombia"}
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

@blueprint.route("/login")
def login():
   return render_template("login.html")

@blueprint.route("/register")
def register():
   return render_template("register.html")

@blueprint.route("/reservations")
def reservations():
    return render_template("reservations.html")