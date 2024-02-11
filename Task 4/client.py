# Write a program to create a server that listens to port 54 using stream sockets . Write a simple client program to connect to the server. send multiple text messages from the client to the server .Send multiple text messages from the client to the server and vice-versa. When either party types BYE close the connection

# client

import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 54))

while (message := input()) != "BYE":
    c.sendall(message.encode())
    if (data := c.recv(1024).decode()) == "BYE":
        print("Received: ", data)
        break
    print("Received: ", data)
