from errorResponse import ErrorResponse
from database.database import Database
import bcrypt


class UserLoginChecker:
    def __init__(self):
        self.db_wrapper = Database()

    def user_is_valid(self, user_data: dict) -> dict:
        """
        takes:
        {
        'email': str,
        'password': str
        }

        checks if:
        - input keys are existing
        - user exists
        - password correct

        then returns as dict:
        {
        'error': str,
        'session': str|Null
        }
        """

        response = {
            "error": "",
            "session": None
        }

        try:
            email = user_data["email"]
            password = user_data["password"]
        except KeyError:
            error = ErrorResponse("json key not found")
            response.update(error.get())

        else:
            if self._get_user_existing_by_email(email):
                hashed = self._get_password_hash_by_email(email)

                try:
                    if self._is_password_matching(password, hashed):
                        response["session"] = self._get_session_id_by_email(email)
                    else:
                        error = ErrorResponse("incorrect password")
                        response.update(error.get())
                except ValueError:  # raised by bcrypt if hash is invalid
                    error = ErrorResponse("invalid hash from database")
                    response.update(error.get())

        return response

    def _is_password_matching(self, password: str, hashed: str) -> bool:
        password_encoded = password.encode("utf8")
        hashed_encoded = hashed.encode("utf8")
        return bcrypt.checkpw(password_encoded, hashed_encoded)

    def _get_user_existing_by_email(self, email: str) -> bool:
        return self.db_wrapper.existUser(email)

    def _get_password_hash_by_email(self, email: str) -> str:
        return self.db_wrapper.getUserPassword(email)

    def _get_session_id_by_email(self, email: str) -> str:
        # TODO generate and save session id
        return "some nice session id"
