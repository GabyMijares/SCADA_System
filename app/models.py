from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timedelta
from app.helper import translate
import os
import base64


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return '<User {}>'.format(self.username)   

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grp = db.Column(db.Integer, index=True)
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

    def to_dict(self):
        data = {
            'id':self.id,
            'volt_pe':self.volt_pe,
            'volt_ky':"Si hay" if (self.volt_ky >200) else "No hay",
            'volt_bat':self.volt_bat,
            'var_tqc':translate['conv_tqc'][self.var_tqc],
            'var_tsb':translate['conv_tsb'][self.var_tsb],
            'corriente':self.corriente,
            'presion':self.presion,
            'alarma':translate['conv_alarmas'][self.alarma],
            'encendido':translate['conv_status'][self.encendido],
            'fecha': self.fecha.isoformat() + 'Z'
        }
        return data
