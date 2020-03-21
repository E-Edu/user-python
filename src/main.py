import json

from flask import Flask, request, jsonify

from response import *
from userRegistrar import UserRegistrar
from database import database as db


app = Flask(__name__)
user_registrar = UserRegistrar()
database = db.Database()
database.connect()
database.setup()

@app.route('/')
def main():
    return 'Team User-Microservice'


@app.route('/user/register', methods=['POST'])
def user_register():
    global content
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    response = user_registrar.register_user_if_valid(content)
    return response.get_json_value(), response.get_code()


@app.route('/user/verify', methods=['PATCH'])
def user_verify():
    return 'and some verify stuff here'


@app.route('/user/login', methods=['POST'])
def user_login():
    return 'some login magic here'


@app.route('/user/info', methods=['POST'])
def user_info():
    return 'info responses here'


@app.route('/user/update', methods=['PUT'])
def user_update():
    return 'and update responses here'


@app.route('/user/session', methods=['POST'])
def user_session():
    return 'or some session checks there'


if __name__ == '__main__':
    app.run(port=4450, threaded=True)
