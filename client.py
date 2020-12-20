import socket
import os

s = socket.socket()
print("\n\nSocket successfully created")

host = input(str("Enter host address of the server: "))
port = 8080
s.connect((host, port))
print("Connected to " + str(host))

filename = input(str("***Receiving file***\nEnter a name for the incoming file: "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
print("The file has been received successfully\n\n")
file.close()

s.close()
