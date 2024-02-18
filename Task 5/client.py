# client
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 55))

c.sendall("test.txt".encode())
content = c.recv(1024).decode()
print(content)

c.close()
