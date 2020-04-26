from flask_restful import Resource, reqparse
from flask import request
from user_ms import db
from user_ms.utils.verifying_email import send_verifying_email

class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, help="email can not be blank")
        parser.add_argument("password", type=str, help="password can not be blank")
        parser.add_argument("first_name", type=str, help="first_name can not be blank")
        parser.add_argument("last_name", type=str, help="last_name can not be blank")
        parser.add_argument("teacher_token", type=str, help="teacher_token can not be blank")

        data = parser.parse_args()
        header = request.headers.get('Authorization')
        path = "/user"

        db_data = User
