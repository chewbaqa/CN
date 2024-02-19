import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 56))
s.listen()

while True:
    conn, addr = s.accept()
    file_name = conn.recv(1024).decode()

    with open(file_name, "rb") as file:
        content = file.read()

    conn.sendall(content)
    print(f"File '{file_name}' has been sent to the client.")
    conn.close()
