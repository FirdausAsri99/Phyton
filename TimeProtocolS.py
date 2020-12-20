import socket
import os
from _thread import *
import time
import datetime
from time import sleep
import sys
from datetime import timedelta

serversocket = socket.socket()

host = socket.gethostname()
port = 8888
serversocket.bind((host,port))
serversocket.listen(5)

def thread_client(connection):
   connection_send(str.encode("Welcome to the server"))
   while True:
      data = connection.recv(2048)
      reply = 'Server Says: ' + data.decode("utf-8")

   connection.sendall(str.encode(reply))


while True:
	clientsocket,addr = serversocket.accept()
	tm = clientsocket.recv(1024)
	print(tm.decode('utf-8'))
	a = tm.decode('utf-8')
	if a == '1':
		currentTime=datetime.datetime.now().strftime("%A %H:%M:%S %p")
		clientsocket.send(str(currentTime).encode())
