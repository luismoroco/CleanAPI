from flask import Flask

from extensions.routes_extension import register_routes
from extensions.db_connection import configDatabase

def createApp():
    app = Flask(__name__)
    app.config['ERROR_404_HELP'] = False

    configDatabase(app)
    register_routes(app)
    return app