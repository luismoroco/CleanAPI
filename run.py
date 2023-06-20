from application import createApp 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from extensions.db_connection import db
import logging as logg
import os 

load_dotenv(dotenv_path='.flaskenv')

app = createApp()

SQLAlchemy(app)
if __name__ == '__main__':
    logg.basicConfig(level=logg.DEBUG, format='%(threadName)s: %(message)s')

    app.run(debug=bool(os.getenv('DEBUG')), 
            port=int(os.getenv('PORT')))