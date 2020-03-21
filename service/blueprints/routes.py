from flask import Blueprint, request, jsonify
from service.usecases.signup import *
from service.usecases.login import *
from service.usecases.info import *
from service import database
from service.role import *

routes = Blueprint('routes', __name__)


@routes.route('/')
def main():
    return 'Team User-Microservice'


# Create User
@routes.route('/user', methods=['POST'])
def user_register():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    response = signup(content)
    return response.get_json_value(), response.get_code()


# Login User
@routes.route('/user/login', methods=['POST'])
def user_login():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    response = login(content)
    return response.get_json_value(), response.get_code()


# Get User Info
@routes.route('/user/<uuid>/info', methods=['GET']) # TODO not REST compliant
def user_info():
    try:
        req_body = json.loads(request.data)
    except ValueError:
        error = ErrorResponse('JSON expected', 400)
        return jsonify(error.get_description()), error.get_code()
    response = info(req_body)
    return response.get_json_value(), response.get_code()



# Set User Info
@routes.route('/user', methods=['PUT']) # TODO not REST compliant
def user_update():
    return 'and update responses here'


# Verify Email
@routes.route('/user/verify', methods=['PATCH'])
def user_session():
    return 'or some email checks there'


# Check User Session
@routes.route('/user/session', methods=['POST'])
def user_session():
    return 'or some session checks there'



