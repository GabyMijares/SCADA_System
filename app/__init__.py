from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask.json import JSONEncoder
import calendar
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)

@app.template_filter('duration')
def caps(delta):
    return str(delta).split('.')[0]

@app.template_filter('post_icon')
def post_icon(delta):
    conv = {"info":"create", "danger":"build", "warning":"warning", "success":"assignment_turned_in"}
    return conv[delta]

@app.template_filter('post_color')
def post_color(delta):
    conv = {"info":"info", "danger":"danger", "warning":"warning", "success":"success"}
    return conv[delta]


from app import routes, models