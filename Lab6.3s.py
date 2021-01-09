import socket
import math
import errno
import sys
from multiprocessing import Process

def ProcessStart(server):
	while True:
		ser = server.recv(1024).decode()

		if ser == '1':
			num = server.recv(3).decode()
			base = server.recv(2).decode()
			sol = math.log(float(num),float(base))

		elif ser == '2':
			num = server.recv(1024).decode()
			sol = math.sqrt(float(num))

		elif ser == '3':
			num = server.recv(1024).decode()
			sol = math.exp(float(num))

		elif ser == '0':
			server.close()
			break


		server.sendall(str(sol).encode())

if __name__ == '__main__':

	s = socket.socket()
	host = ''
	port = 8888

	try:
		s.bind((host,port))
		print('Waiting for connection')
	except socket.error as e:
		print (str(e))
		sys.exit()

	s.listen(5)
	while True:
		try:
			server,add = s.accept()
			print('Successful connection\n')

			p = Process(target = ProcessStart, args=(server,))
			p.start()

		except socket.error:
			print('an error has occurred')

	s.close()
