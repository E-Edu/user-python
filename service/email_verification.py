class EmailVerification:
    def __init__(self, user_uuid, verification_code, created):
        self.user_uuid = user_uuid
        self.verification_code = verification_code
        self.created = created
