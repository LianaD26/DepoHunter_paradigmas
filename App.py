import os
from flask import Flask 
from src.view import view_user

app = Flask(__name__)     

app.secret_key = os.urandom(24)

app.register_blueprint(view_user.blueprint)

if __name__=='__main__':
   app.run( debug=True )