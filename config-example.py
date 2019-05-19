import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI= 'mysql://root@localhost/SCADA_System'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER= os.path.join( basedir, 'app\\static\\uploads')
    POSTS_PER_PAGE=5
    ROWS_PER_TABLE=10
    MAIL_ENABLED = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "smtp.gmail.com"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['example@example.com']