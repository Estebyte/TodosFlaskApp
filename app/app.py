from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

#Create a function to create the app and avoinding execute all the code when importing app.py
def create_app():
    app = Flask(__name__, template_folder="templates")

    #Connect to SQLite, as an example
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db" #sqlite:///<path>
    #Disable track modifications (optional)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    #Initialize the app
    db.init_app(app)

    #Import register_routes() IN create_app() to avoid circular imports
    from routes import register_routes
    register_routes(app, db)

    #Set migrate
    migrate = Migrate(app, db)

    return app