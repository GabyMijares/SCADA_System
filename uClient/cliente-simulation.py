import urllib3
import time
import json

http = urllib3.PoolManager()

while True:
	data = {
	'volt_pe': 200,
	'volt_ky': 200,
	'volt_bat': 15,
	'var_tqc': 2,
	'var_tsb': 1,
	'corriente': 50,
	'presion': 1,
	'alarma': 0,
	'encendido': 1
	}
	encoded_data = json.dumps(data).encode('utf-8')
	r = http.request(
		'POST',
		'http://127.0.0.1:5000/api/v0/send_data',
		body=encoded_data,
		headers={'Content-Type': 'application/json'})
	r = json.loads(r.data.decode('utf-8'))

	if r['msg']:
		if r['msg'] == 'N':
			print('ENCENDIENDO!')
		elif r['msg'] == 'O':
			print('APAGANDO!')
	# Tiempo entre ciclos
	time.sleep(3)