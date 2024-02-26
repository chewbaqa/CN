import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_name = input("Enter the name of the binary file you want to request: ")
s.sendto(file_name.encode(), ("localhost", 59))

data, addr = s.recvfrom(1024)
print(data.decode())

s.close()
