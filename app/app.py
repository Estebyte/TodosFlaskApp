from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from extensions import login_manager, db, bcrypt

#Create a function to create the app 
def create_app():
    app = Flask(__name__, template_folder="templates")

    #Connect to SQLite, as an example
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db" #sqlite:///<path>
    #Disable track modifications (optional)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    #Set secret key
    app.config["SECRET_KEY"] = "notaverysecuresecretkey"

    #Register blueprints
    from blueprints.todos.todos_routes import todos
    app.register_blueprint(todos)
    
    from blueprints.details.details_routes import details
    app.register_blueprint(details)

    from blueprints.auth.auth_routes import auth
    app.register_blueprint(auth)

    #Extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    """
    Since SQLite3 has no "ALTER TABLE", render_as_batch = True 
    allows alembic to make changes in a table by creating a copy of it
    with the changes applied and deleting the old table.
    """
    migrate = Migrate(app, db, render_as_batch=True)

    #Define to the login manager what it means to log a user
    from models import User
    @login_manager.user_loader
    def log_user(u_id):
        return User.query.get(u_id)
    
    #Set the view to redirect if the user is not authenticated
    login_manager.login_view = 'auth.login'

    # #Handle unauthorized cases
    # @login_manager.unauthorized_handler
    # def unauthorized_callback():
    #     #Do here whatever you want
    #     return "Sorry! You have to login to access this"
    
    #Import register_routes() IN create_app() to avoid circular imports
    from routes import register_routes
    register_routes(app, db, bcrypt)

    return app