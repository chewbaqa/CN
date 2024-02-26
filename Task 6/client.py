import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect_ex(("localhost", 56))
c.sendall("test.bin".encode())

content = c.recv(1024).decode()
print(content)
c.close()
