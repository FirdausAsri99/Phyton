import socket
import sys
import datetime
import time
from time import sleep

s = socket.socket()

host = "192.168.42.3"

port = 8888

print(f"Connecting to {host}:{port}")

s.connect((host, port))
print("connected")
time.sleep(1)

#Front page function
def fmenu():
	print("-------------------------------THE TIME ZONE-------------------------")
	print("|1| Go to time zone")
	print("|0| Exit the program")
	while True:
		pick = input("Enter your choice:")
		if pick == '1':
			Datetime()
		elif pick == '0':
			break
		else:
			print("invalid choice")
			fmenu()
	sys.exit()

#Date tiem menu
def Datetime():
	print("This is a simple time zone")
	print("[1] To check for today day and time")
	print("[2] to go back to the Main menu")
	print("[0] to exit the program")
	while True:
		sel = input("Enter your choice")
		if sel == '1':
			s.send(sel.encode())
			msg = s.recv(36)
			print("Today time :%s" % msg.decode('utf-8'))
		elif sel == '2':
			fmenu()
		elif sel == '0':
			sys.exit()
		else:
			print("No input from server")




fmenu()
