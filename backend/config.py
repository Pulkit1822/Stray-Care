import os
from datetime import timedelta

class Config:
    SECRET_KEY= os.getenv('SECRET_KEY', 'my-secret-key')
    SQLALCHEMY_DATABASE_URI= os.getenv('DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JWT_SECRET_KEY= os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES= timedelta(hours=1)
    GOOGLE_CLOUD_PROJECT= os.getenv('GOOGLE_CLOUD_PROJECT')
    GOOGLE_APPLICATION_CREDENTIALS= os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
