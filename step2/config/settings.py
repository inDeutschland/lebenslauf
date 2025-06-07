# config/settings.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    DEBUG = True
