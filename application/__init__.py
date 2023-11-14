from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.config import DevConfig

from flask_login import LoginManager


app = Flask(__name__)
app.static_folder = '../static'
app.template_folder = 'templates'

app.config.from_object(DevConfig)

login_manager = LoginManager()

login_manager.init_app(app)
db = SQLAlchemy(app)
