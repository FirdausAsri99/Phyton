import socket
import sys
import os

cs = socket.socket()
host = '192.168.42.3'
port = 8888

try:
	cs.connect((host,port))
	print('Successfull Connect')
except socket.error as e:
	print (str(e))

while True:
	print('--------------------Mathematical choice----------------------')
	print('1-Log expression')
	print('2-Square root')
	print('3-Exponential expression')
	print('0-exit')

	equat = input('Enter your choice:')
	cs.send(equat.encode())
	os.system('clear')
	if equat == '1':
		print('Log fucntion')
		num=input('Enter number:')
		b = input('Enter base:')
		cs.send(num.encode())
		cs.send(b.encode())
		total=cs.recv(1024)

		print('Solution :'+ str(total.decode('utf-8')))
	elif equat == '2':
		sol = True
		while sol:
			print('Square root function')
			num =input('Enter number:')
			if int(num)> -1:
				cod = False
				cs.send(num.encode())
				total=cs.recv(1024)
			else:
				print('Enter positive number')

		print('Solution :'+ str(total.decode('utf-8')))

	elif equat == '3':
		print('Exponential funciton')
		num=input('Enter number:')
		cs.send(num.encode())
		total=cs.recv(1024)
		print('Solution :'+ str(total.decode('utf-8')))

	elif equat == '0':

		cs.close()
		sys.exit()
	else:
		print('Invalid input')
