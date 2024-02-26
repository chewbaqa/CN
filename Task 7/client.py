# client
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect_ex(("localhost", 57))

file_name = input("Enter the file name: ")
c.sendall(file_name.encode())
content = c.recv(1024).decode()
print(content)

c.close()
