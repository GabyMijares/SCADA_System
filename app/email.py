from flask import render_template
from flask_mail import Message
from threading import Thread
from app import app,mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

def send_alarm_email(emails, alarm_msg):
    send_email('Alarma. Sistema Scada.',
               sender=app.config['ADMINS'][0],
               recipients=emails,
               text_body=render_template('email/alarm_email.txt', type=alarm_msg),
               html_body=render_template('email/alarm_email.html', type=alarm_msg))