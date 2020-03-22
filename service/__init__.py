from flask import Flask
from service.database import *
from service.blueprints import *

db = Database()
db.connect()
db.setup()

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(error)
