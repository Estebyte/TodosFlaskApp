from flask import Blueprint, render_template, redirect, url_for, request
from extensions import db, bcrypt
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
        username = request.form.get("username")
        password = request.form.get("password")

        #Hash the password
        hashed_password= bcrypt.generate_password_hash(password).decode("utf-8")

        #Save user in the db
        try:
            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()

        except Exception as error:
            context = {
                "error" : error
            }
            return render_template("error.html", **context)
        
        return redirect(url_for("login"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
