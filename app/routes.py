from app import app, db
from flask import render_template, flash, redirect, request, url_for, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Respuesta
from app.forms import LoginForm
from werkzeug.urls import url_parse

state = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Email o contraseña invalida')
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
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():

    q = Respuesta.query.order_by(Respuesta.id.desc()).first_or_404()
    context = { 
    'data': q,
    'conv_tqc':{1:'Full', 2:'3/4', 3:'1/2', 4:'1/4', 5:'Dañado'},
    'conv_tsb':{1:'Full', 2:'Vacio', 3:'Llenando'},
    'conv_status':{0:'OFF', 1:'ON'},
    'conv_alarmas':{0:'Ok', 1:'Falla inicio', 2:'Alta temp', 3:'Baja presion', 4:'Sobrevelocidad'},
    'state':state
    }
    return render_template('dashboard.html',  context=context)


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
    msg = {'msg':False}
    if 'action' in state.keys():
        msg.update({'msg': 'N' if state.pop('action') else 'O'})
    return jsonify(msg)

@app.route('/api/v0/switch', methods=['POST'])
def switch():
    data  = request.get_json()
    print(data)
    state.update(data)
    status = {'msg':'ok'}
    return jsonify(status)