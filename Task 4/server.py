# Write a program to create a server that listens to port 54 using stream sockets . Write a simple client program to connect to the server. send multiple text messages from the client to the server .Send multiple text messages from the client to the server and vice-versa. When either party types BYE close the connection
# server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 54))
s.listen()
conn, _ = s.accept()

while (data := conn.recv(1024).decode()) != "BYE":
    print("Received: ", data)
    if (message := input()) == "BYE":
        conn.sendall(message.encode())
        break
    conn.sendall(message.encode())
