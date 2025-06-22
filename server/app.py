from flask import Flask
from server.config import Config
from server.extensions import db, migrate, jwt
from server.controllers import all_controllers
from dotenv import load_dotenv
load_dotenv() 

def create_app():
  # ✅ Move here to make sure it runs when app is created

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints (controllers)
    for controller in all_controllers:
        app.register_blueprint(controller)

    return app
