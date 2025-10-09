from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.config import Config
from app.models import db
from app.routes import register_routes


# Creea la app con todas las configuraciones
def create_app():


    # Inicia la api con todas las configuracicones
    app = Flask(__name__)
    app.config.from_object(Config)


    # Configura las políticas de seguridad del navegador
    CORS(app)
    

    # Vincula la api con la clase SQLAlchemy
    db.init_app(app)


    # Registro cada uno de las rutas
    register_routes(app)


    return app
