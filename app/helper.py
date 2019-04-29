from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

translate = {
    'conv_tqc':{1:'Full', 2:'3/4', 3:'Medio', 4:'1/4', 5:'Dañado'},
    'conv_tsb':{1:'Full', 2:'Vacio', 3:'Llenando'},
    'conv_status':{0:'OFF', 1:'ON'},
    'conv_alarmas':{0:'Ok', 1:'Falla al encender la planta eléctrica.',\
                    2:'Alta temperatura en el motor de la planta eléctrica.', \
                    3:'Baja presion del aceite del motor.', \
                    4:'Sobrevelocidad en el motor de la planta eléctrica.'},
}

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_response(400, message)
