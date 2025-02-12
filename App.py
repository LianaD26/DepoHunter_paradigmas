from flask import Flask 

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
# from flask import render_template

from src.view import view_user

app = Flask(__name__)     

app.register_blueprint(view_user.blueprint)

if __name__=='__main__':
   app.run( debug=True )