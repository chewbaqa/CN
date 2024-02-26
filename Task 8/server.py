import socket
import threading


def handle_client(addr, data):
    file_name = data.decode()
    print(f"Client {addr} requested file: {file_name}")
    with open(file_name, "rb") as file:
        content = file.read()
    s.sendto(content, addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 59))

while True:
    data, addr = s.recvfrom(1024)
    thread = threading.Thread(target=handle_client, args=(addr, data))
    thread.start()
