from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import *
admin = Admin(app)
admin.add_view(ModelView(Blog, db.session))
admin.add_view(ModelView(Tag, db.session))

