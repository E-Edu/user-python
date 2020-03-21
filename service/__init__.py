from flask import Flask
from service.database import database as db
from service.blueprints.routes import routes
from service.blueprints.error import error

database = db.Database()
database.connect()
database.setup()

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(error)
