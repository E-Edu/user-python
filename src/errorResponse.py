class ErrorResponse:
	def __init__(self, error_message: str, response_code: int):
		self.errorMessage = error_message
		self.response_code = response_code

	def get_description(self) -> dict:
		return {"error": self.errorMessage}

	def get_code(self) -> int:
		return self.response_code

	def set(self, error_message: str, response_code: int):
		self.errorMessage = error_message
		self.response_code = response_code