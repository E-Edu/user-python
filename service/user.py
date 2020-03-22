class User:
    def __init__(self, uuid, email, password, first_name, last_name, status, role, created):
        self.uuid = uuid
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.role = role
        self.created = created
