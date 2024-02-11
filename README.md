# What is a socket?
Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

### Socket API Overview
The primary socket API functions and methods are:

- **socket()**: Create a new socket.
- **bind()**: Associate the socket with a specific network address and port.
- **listen()**: Enable the socket to accept incoming connections.
- **accept()**: Accept a connection, returning a new socket for communication with the client.
- **connect()**: Initiate a connection to a remote server.
- **connect_ex()**: Same as connect(), but returns an error code instead of raising an exception on failure.
- **send()**: Send data over the socket.
- **recv()**: Receive data from the socket.
- **close()**: Close the socket, releasing the associated resources.
# Task 3

1. Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and close the connection.

2. Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and the server to the client and close the connection.

3. Write a program to  create a client that listen to port 12000 using stream sockets .write a simple client program that sends a lower case letters and the server converts into a upper case letters and close the connection.
# Task 4
1. Write a program to create a server that listens to port 54 using stream sockets . Write a simple client program to connect to the server. send multiple text messages from the client to the server .Send multiple text messages from the client to the server and vice-versa. When either party types BYE close the connection