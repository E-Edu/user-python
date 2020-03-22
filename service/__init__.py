from flask import Flask
from service.blueprints import *

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(error)
