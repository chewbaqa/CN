# server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 55))
s.listen()

conn, addr = s.accept()

file_name = conn.recv(1024).decode()
with open(file_name, "r") as file:
    content = file.read()
conn.sendall(content.encode())

conn.close()
