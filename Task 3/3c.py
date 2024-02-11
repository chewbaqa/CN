# 3. Write a program to  create a client that listen to port 12000 using stream sockets .write a simple client program that sends a lower case letters and the server converts into a upper case letters and close the connection.
# client

import socket

c = socket.socket()
c.connect(("localhost", 12000))
c.sendall(b"hello there")
print(c.recv(1024).decode())
c.close()
