from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

#Create a function to create the app and avoinding execute all the code when importing app.py
def create_app():
    app = Flask(__name__, template_folder="templates")

    #Connect to SQLite, as an example
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db/test.db" #sqlite:///<path>

    #Initialize the app
    db.init_app(app)

    #imports later on

    #Set migrate
    migrate = Migrate(app, db)

    return app