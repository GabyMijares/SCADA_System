from app import app, db
from flask import render_template, flash, redirect, request, url_for, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Respuesta
from app.forms import LoginForm
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/dashboard')
@login_required
def dashboard():
    q = Respuesta.query.all()
    context = { 'data': q}
    return render_template('dashboard.html', title='Sign In', context=context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/api/v0/send_data', methods=['POST'])
def send_data():
    data  = request.get_json()
    print(data)
    resp = Respuesta(volt_pe=data['volt_pe'], volt_ky=data['volt_ky'], \
        volt_bat=data['volt_bat'], var_tqc=data['var_tqc'], \
        var_tsb=data['var_tsb'], corriente=data['corriente'], \
        presion=data['presion'], alarma=data['alarma'], \
        encendido=data['encendido'] )
    db.session.add(resp)
    db.session.commit()
    status = {'msg':'N'}
    return jsonify(status)
