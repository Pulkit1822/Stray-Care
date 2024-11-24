from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from api import create_api
from services import init_services
from utils.config import Config

db= SQLAlchemy()
jwt= JWTManager()

def create_app(config_class=Config):
    app= Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    
    # Initialize services
    init_services(app)
    
    # Register API blueprints
    create_api(app)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__== '__main__':
    app= create_app()
    app.run(host='0.0.0.0', port=5000)