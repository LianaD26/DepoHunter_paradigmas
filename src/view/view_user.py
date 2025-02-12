from flask import Blueprint, render_template

blueprint = Blueprint( "view_user", __name__, template_folder="templates" )

alojamientos = [
   {"id": 100, "nombre": "Alojamiento1", "precio": 123000, "imagen": "https://www.revistaaxxis.com.co/wp-content/uploads/2022/08/casa_cinco_9.jpg"},
   {"id": 101, "nombre": "Alojamiento2", "precio": 150000, "imagen": "https://arquitectopablorestrepo.com/wp-content/uploads/2024/01/Casa-Moderna-Costa-Azul-6.jpg"},
   {"id": 102, "nombre": "Alojamiento3", "precio": 95000, "imagen": "https://revistaaxxis.com.co/wp-content/uploads/2019/09/llano-axxis1.jpg"}
]

@blueprint.route("/")
def home():
   # del controlador que va a hacer David debe estar una función que retorne el select de todos los alojamientos de la BD
   # eso lo va a retornar como una lista de objetos de tipo Alojamiento, y yo voy a mostrar cada uno de sus atributos
   # a el html le paso el objeto
   # en la siguiente variable lo que hago es guardar esa lista después de haber importado esa función
   # alojamientos = obtener_alojamientos()
   # prueba con (id, nombre, precio)
   # Simulación de base de datos de alojamientos
   return render_template("home.html", alojamientos=alojamientos)

@blueprint.route("/alojamiento/<int:id>")
def alojamiento_detalle(id):
    alojamiento = next((a for a in alojamientos if a["id"] == id), None)
    if alojamiento is None:
        return "Alojamiento no encontrado", 404
    return render_template("detail.html", alojamiento=alojamiento)

@blueprint.route("/Login")
def Login():
   return render_template("login.html")

@blueprint.route("/Register")
def Register():
   return render_template("register.html")