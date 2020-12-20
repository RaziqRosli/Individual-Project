import socket
import os
from _thread import *

ThreadCount = 0
s = socket.socket()
print("\n\nSocket successfully created")

host = socket.gethostname()
port = 8080
s.bind((host, port))
print("socket binded to " + str(port))
print("server's ip address is 192.168.0.200")

s.listen(5)
print("socket is listening")

def threaded_client(connection):

	filename = input(str("***Sending file***\nEnter the name of the file: "))
	file = open(filename, 'rb')
	file_data = file.read(1024)
	Client.send(file_data)
	print("The file has been sent successfully\n\n")

	connection.close()

while True:

	Client, address = s.accept()

	print('Connected to: ' + address[0] + ':' + str(address[1]))

	start_new_thread(threaded_client, (Client, ))

	ThreadCount += 1

	print('Thread Number: ' + str(ThreadCount) + '\n')

s.close()
