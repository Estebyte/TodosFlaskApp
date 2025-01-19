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

        except Exception as error:
            db.session.rollback()
            context = {
                "error" : error
            }
            return render_template("error.html", **context)
        else:
            db.session.commit()
            return redirect(url_for("auth.login"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
        
    #Save user in the db
    elif request.method == "POST":
        #Get values from the form
        username = request.form.get("username")
        password = request.form.get("password")

        #Get user
        user = User.query.filter(User.username == username).first()
        
        #Check the password
        try:
            if not user or not bcrypt.check_password_hash(user.password, password):
                raise Exception("Incorrect login credentials")

        except Exception as error:
            context = {
                "error" : error
            }            
            return render_template("error.html", **context)   
        else:
            login_user(user)
            return redirect(url_for("index"))
        
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
