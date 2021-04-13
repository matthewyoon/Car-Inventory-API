from flask import Flask
from config import Config

from .site.routes import site
from .authentication.routes import templates

from flask_migrate import Migrate 
from .models import db as root_db

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(templates)

root_db.init_app(app)
migrate = Migrate(app,root_db)

from vehicle_inventory import models