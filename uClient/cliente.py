import serial as s
import urllib3
import time
import json

try:
	ser = s.Serial('COM1',timeout=1)
except Exception as e:
	print('Error')

http = urllib3.PoolManager()

email= "wgaby@gmail.com"
password="123456"
token=""

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

	if token:
		encoded_data = json.dumps(data).encode('utf-8')
		headers = ({'Content-Type': 'application/json','Authorization': 'Bearer {}'.format(token)})
		r = http.request('POST','http://192.168.1.114:5000/api/v0/send_data',body=encoded_data,	headers=headers)
		if r.status == 200:
			r = json.loads(r.data.decode('utf-8'))
			if 'msg' in r.keys():
				if r['msg'] == 'N':
					print('APAGANDO!')
					ser.write(b'N')
				elif r['msg'] == 'O':
					print('ENCENDIENDO!')
					ser.write(b'O')
		else:
			headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(email,password))
			headers.update({'Content-Type': 'application/json'})
			r = http.request('POST','http://192.168.1.114:5000/api/v0/tokens', headers=headers)
			r = json.loads(r.data.decode('utf-8'))
			if 'token' in r.keys():
				token = r['token']
				print('Nuevo token!')
	else:
			headers = urllib3.util.make_headers(basic_auth='{}:{}'.format(email,password))
			headers.update({'Content-Type': 'application/json'})
			r = http.request('POST','http://192.168.1.114:5000/api/v0/tokens', headers=headers)
			r = json.loads(r.data.decode('utf-8'))
			if 'token' in r.keys():
				token = r['token']
				print('Nuevo token!')

	time.sleep(5)