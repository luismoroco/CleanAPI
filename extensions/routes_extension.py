from apps.api.item.item import item as item_api 
from apps.api.user.user import user as user_api

from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Register routes with blueprint
    """
    app.register_blueprint(user_api)
    app.register_blueprint(item_api)