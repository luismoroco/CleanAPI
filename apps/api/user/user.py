from flask import Blueprint

user = Blueprint('users', __name__, url_prefix='/users')

@user.route('/')
def index():
    return 'users home'

@user.route('/new')
def addUser():
    return 'adding new user'
