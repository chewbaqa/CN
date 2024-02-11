# 1.Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and close the connection.
# server

import socket

s = socket.socket()
s.bind(("", 53))
s.listen()
conn, _ = s.accept()
print(conn.recv(1024).decode())
