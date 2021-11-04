from flask import Flask
import os
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .main import main
from .models import *

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    
    app.register_blueprint(main)

    return app

