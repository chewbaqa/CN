# server
import socket
import threading


def handle_client(conn, addr):
    file_name = conn.recv(1024).decode()
    print(f"Client {addr} requested file: {file_name}")
    with open(file_name, "rb") as file:
        content = file.read()
    conn.sendall(content)
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 57))
s.listen()

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
