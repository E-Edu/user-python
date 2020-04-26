from flask_restful import Resource, reqparse
from flask import request
from user_ms import db
from user_ms.response import response, Status
from user_ms.config import JWT
import jwt

class SetUserInfo(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, help="email can not be blank")
        parser.add_argument("first_name", type=str, help="first_name can not be blank")
        parser.add_argument("last_name", type=str, help="last_name can not be blank")
        data = parser.parse_args()
        header = request.headers.get('Authorization')
        path = "/user"

        try:
            userdata = jwt.decode(header, JWT.JWT_SEC, JWT.JWT_ALGORITHMS)
        except Exception as e:
            print(e)
            return response(401, Status.c_401, path, Status.cm_1)

        db_data = User(email=data["email"], #TODO Check funk name and import
                    first_name=data["first_name"], 
                    last_name=data["last_name"],
        )
        db_data.save_todb() #TODO Check funk name
        return response(200, Status.c_200, path)