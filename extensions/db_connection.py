from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from flask import Flask
import logging as logg

envPath = os.path.join(os.path.dirname(__file__), '..', '.flaskenv')
load_dotenv(dotenv_path=envPath)

db = SQLAlchemy()

def configDatabase(app: Flask) -> None:
    """
    Configuring DB
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('SQLALCHEMY_DATABASE_URI'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))    
