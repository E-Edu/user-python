from flask import Flask
from flask_cors import CORS
from service.blueprints import *

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(error)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
