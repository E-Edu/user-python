from flask import Flask
from service.database import *
from service.blueprints import *

database = Database()
database.connect()
database.setup()

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(error)
