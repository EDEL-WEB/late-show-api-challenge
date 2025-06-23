from flask import Flask
from server.config import Config
from server.extensions import db, migrate, jwt
from server.controllers import all_controllers
from dotenv import load_dotenv
load_dotenv() 

def create_app():
  

    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    
    for controller in all_controllers:
        app.register_blueprint(controller)

    return app
