import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect_ex(("localhost", 55))

file_name = input("Enter the name of the file you want to request: ")
c.sendall(file_name.encode())

content = c.recv(1024).decode()
print(content)

c.close()
