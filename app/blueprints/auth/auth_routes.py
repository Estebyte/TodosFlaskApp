from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from models import User
#Import flask_login functions
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    
    #Save user in the db
    elif request.method == "POST":
        #Get values from the form
        user = request.form.get("username")
        password = request.form.get("password")

        #Hash the password
        #hashed_password = 

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("index"))
