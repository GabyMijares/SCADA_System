import serial as s
import urllib3
import time
import json

try:
	ser = s.Serial('COM1',timeout=1)
except Exception as e:
	print('Error')

http = urllib3.PoolManager()

while True:
	ser.write(b'Z')
	trama = ser.readline()
	trama = trama.decode('utf-8')[7:-2]
	valores = [float(x) for x in trama.split('*-*')]
	data = {
	'volt_pe': valores[0],
	'volt_ky': valores[1],
	'volt_bat': valores[2],
	'var_tqc': valores[3],
	'var_tsb': valores[4],
	'corriente': valores[5],
	'presion': valores[6],
	'alarma': valores[7],
	'encendido': valores[8]
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
			ser.write(b'N')
		elif r['msg'] == 'O':
			print('APAGANDO!')
			ser.write(b'O')

	# Tiempo entre ciclos
	time.sleep(3)