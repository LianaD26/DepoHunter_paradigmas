from flask import Blueprint, render_template

blueprint = Blueprint( "view_user", __name__, "templates" )

@blueprint.route("/")
def Home():
   return render_template("home.html")