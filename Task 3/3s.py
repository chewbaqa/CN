# 3. Write a program to  create a client that listen to port 12000 using stream sockets .write a simple client program that sends a lower case letters and the server converts into a upper case letters and close the connection.
# server

import socket

s = socket.socket()
s.bind(("localhost", 12000))
s.listen()
conn, _ = s.accept()
data = conn.recv(1024).decode()
conn.sendall(data.upper().encode())
conn.close()
