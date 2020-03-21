class ErrorResponse:
    def __init__(self, errorMessage):
        self.errorMessage = errorMessage

    def get(self):
        return {"error":self.errorMessage}

    def set(self, errorMessage):
        self.errorMessage = errorMessage