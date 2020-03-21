import json

from flask import Flask, request, jsonify

from errorResponse import ErrorResponse
from userRegistrar import UserRegistrar
import database.database as db


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
        return jsonify(error.get_description()), error.get_code()

    response = user_registrar.register_user_if_valid(content)
    return response.get_description(), response.get_code()


@app.route('/user/verify', methods=['PATCH'])
def user_verify():
    return 'and some verify stuff here'


@app.route('/user/login', methods=['POST'])
def user_login():
    return 'some login magic here'


@app.route('/user/info', methods=['POST'])
def user_info():
    global database
    req_body = None
    try:
        req_body = json.loads(request.data)
    except ValueError:
        error = ErrorResponse('JSON expected', 400)
        return jsonify(error.get_description()), error.get_code()

    if not 'session' in req_body:
        error = ErrorResponse('No session provided', 400)
        return jsonify(error.get_description()), error.get_code()

    if (not 'user' in req_body) or req_body['user'] == None:
        # return information about owner of this session
        pass
    else:
        # return informatin about the provided user
        user_to_query = req_body['user']
        if not utils.is_mail_format(user_to_query) or not database.existsUser(user_to_query):
            error = ErrorResponse('No valid user', 400)
            return jsonify(error.get_description()), error.get_code()

        user_id = database.getUserIdByEmail(user_to_query)
        infos = database.getUserInfo(user_id)

        # TODO: privileged student + report_spammer
        return {
            'teacher': infos[7] == database.Role.TEACHER,
            'admin': infos[7] == database.Role.ADMIN,
            'priviliged_student': False,
            'report_spammer': 0
        }


@app.route('/user/update', methods=['PUT'])
def user_update():
    return 'and update responses here'


@app.route('/user/session', methods=['POST'])
def user_session():
    return 'or some session checks there'


if __name__ == '__main__':
    app.run(port=4450, threaded=True)
