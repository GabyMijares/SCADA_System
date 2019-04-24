from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)   

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    volt_pe = db.Column(db.Float)
    volt_ky = db.Column(db.Float)
    volt_bat = db.Column(db.Float)
    var_tqc = db.Column(db.Integer)
    var_tsb = db.Column(db.Integer)
    corriente = db.Column(db.Float)
    presion = db.Column(db.Float)
    alarma = db.Column(db.Integer)
    encendido = db.Column(db.Boolean)			#encendido = bandera
    fecha = db.Column(db.DateTime, default=datetime.utcnow)