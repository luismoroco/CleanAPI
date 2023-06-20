from flask import Flask

from extensions.routes_extension import register_routes

def createApp():
    app = Flask(__name__)
    app.config['ERROR_404_HELP'] = False

    register_routes(app)
    return app