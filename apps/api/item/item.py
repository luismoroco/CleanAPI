from flask import Blueprint

item = Blueprint('items', __name__, url_prefix='/items')

@item.route('/')
def index():
    return 'items home'

@item.route('/new')
def addItem():
    return 'adding new item'