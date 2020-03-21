import bcrypt


class UserLoginChecker:
    def __init__(self):
        pass

    def user_is_valid(self, user_data: dict) -> dict:
        response = {
            "error": "",
            "Guid": None
        }

        try:
            email = user_data["email"]
            password = user_data["password"]
        except KeyError:
            response["error"] = "json key not found"
        else:
            hashed = self._get_password_hash_by_email(email)
            if self._is_password_matching(password, hashed):
                response["Guid"] = self._get_guid_from(email, hashed)
            else:
                response["error"] = "wrong password"

        return response

    def _is_password_matching(self, password: str, hashed: str) -> bool:
        password_encoded = password.encode("utf8")
        hashed_encoded = hashed.encode("utf8")
        return bcrypt.checkpw(password_encoded, hashed_encoded)

    def _get_password_hash_by_email(self, email: str) -> str:
        # TODO get from db
        return ""

    def _get_guid_from(self, email: str, hashed: str) -> str:
        # TODO generate from email&pw hash&server secret
        return ""

