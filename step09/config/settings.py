# config/settings.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lebenslauf.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
