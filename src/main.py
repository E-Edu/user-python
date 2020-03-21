import json

from flask import Flask, request, jsonify

from src.auth import hash_password, sanitize_user_input, verify_teacher, create_session, create_database_user, verify_password
from src.errorResponse import ErrorResponse

app = Flask(__name__)


@app.route('/')
def main():
    return 'Team User-Microservice'


@app.route('/user/register', methods=['POST'])
def user_register():
    global content
    try:
        content = json.loads(request.data)
    except ValueError:
        return jsonify(ErrorResponse("JSON expected").get()), 400

    email = content["email"]
    password = content["password"]
    first_name = content["first_name"]
    last_name = content["last_name"]
    teacher_token = content["teacher_token"]
    verify_password(teacher_token)
    hashed_password = hash_password(password)

    sanitize_user_input(email, first_name, last_name, teacher_token)
    verify_teacher(teacher_token)
    create_database_user(email, password, first_name, last_name, hashed_password, teacher_token)
    create_session(email)
    return jsonify({}), 201


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
