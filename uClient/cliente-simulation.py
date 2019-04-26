import urllib3
import time
import json
import random as ropa

http = urllib3.PoolManager()

email= "sauloviedoleon@gmail.com"
password="123456"
token=""



while True:
	data = {
	'volt_pe': 200,
	'volt_ky': 200,
	'volt_bat': 15,
	'var_tqc': ropa.choice([1,2,3,4,5]),
	'var_tsb': 1,
	'corriente': 50,
	'presion': 1,
	'alarma': 0,
	'encendido': 1
	}

	if token:
		encoded_data = json.dumps(data).encode('utf-8')
		headers = urllib3.util.make_headers(basic_auth='sauloviedo@gmail.com:123456')
		headers = ({'Content-Type': 'application/json','Authorization': 'Bearer {}'.format(token)})
		r = http.request('POST','http://127.0.0.1:5000/api/v0/send_data',body=encoded_data,	headers=headers)
		if r.status == 200:
			r = json.loads(r.data.decode('utf-8'))
			if 'msg' in r.keys():
				if r['msg'] == 'N':
					print('APAGANDO!')
				elif r['msg'] == 'O':
					print('ENCENDIENDO!')
		else:
			headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(email,password))
			headers.update({'Content-Type': 'application/json'})
			r = http.request('POST','http://127.0.0.1:5000/api/v0/tokens', headers=headers)
			r = json.loads(r.data.decode('utf-8'))
			if 'token' in r.keys():
				token = r['token']
				print('Nuevo token!')
		# Tiempo entre ciclos
	else:
			headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(email,password))
			headers.update({'Content-Type': 'application/json'})
			r = http.request('POST','http://127.0.0.1:5000/api/v0/tokens', headers=headers)
			r = json.loads(r.data.decode('utf-8'))
			if 'token' in r.keys():
				token = r['token']
				print('Nuevo token!')
	time.sleep(5)