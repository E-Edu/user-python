from flask import *


# TODO move


class Response:
    def __init__(self, value: object, code: int):
        self.value = value
        self.code = code

    def get_value(self):
        return self.value

    def get_json_value(self):
        return jsonify(self.get_value())

    def get_code(self):
        return self.code


class ErrorResponse(Response):
    def __init__(self, error_message: str, code: int):
        super().__init__({"error": error_message}, code)
