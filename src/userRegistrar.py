from src.errorResponse import ErrorResponse
import bcrypt
import re


class UserRegistrar:
    def register_user_if_valid(self, user_data: dict) -> ErrorResponse:
        try:
            email = user_data["email"]
            first_name = user_data["first_name"]
            last_name = user_data["last_name"]
            password = user_data["password"]
        except KeyError:
            return ErrorResponse("missing key", 400)

        # key only exists if user wants to register as teacher
        if "teacher_token" in user_data.keys():
            teacher_token = user_data["teacher_token"]
            if not self._is_valid_teacher_token(teacher_token):
                return ErrorResponse("invalid teacher token", 400)

        if not self._is_valid_email(email):
            return ErrorResponse("invalid email", 400)
        if not self._is_valid_name(first_name):
            return ErrorResponse("invalid first name", 400)
        if not self._is_valid_name(last_name):
            return ErrorResponse("invalid last name", 400)
        if not self._is_strong_password(password):
            return ErrorResponse("password too weak", 400)

        # TODO add user to database

        # code 201 = user created
        return ErrorResponse("", 201)

    def _is_valid_teacher_token(self, teacher_token):
        # TODO check if teacher_token is in teacher token db
        pass

    def _is_strong_password(self, password) -> bool:
        if len(password) < 8:
            return False
        elif re.search('[0-9]', password) is None:
            return False
        elif re.search('[a-zA-Z]', password) is None:
            return False
        return True

    def _is_valid_name(self, name) -> bool:
        if re.match(r"^[a-zA-Z]+$", name) is None:
            return False
        elif len(name) < 0:
            return False
        elif len(name) > 32:
            return False
        return True

    def _is_valid_email(self, email) -> bool:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email) is None:
            return False
        elif len(email) > 64:
            return False
        return True
