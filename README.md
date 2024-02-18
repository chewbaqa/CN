# What is a socket?

Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

### Socket API Overview

The primary socket API functions and methods are:

-   **socket()**: Create a new socket.
-   **bind()**: Associate the socket with a specific network address and port.
-   **listen()**: Enable the socket to accept incoming connections.
-   **accept()**: Accept a connection, returning a new socket for communication with the client.
-   **connect()**: Initiate a connection to a remote server.
-   **connect_ex()**: Same as connect(), but returns an error code instead of raising an exception on failure.
-   **send()**: Send data over the socket.
-   **recv()**: Receive data from the socket.
-   **close()**: Close the socket, releasing the associated resources.

# Task 3

1. Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and close the connection.

2. Write a program to create a server that listens to port 53 using Stream sockets. Write a simple client program to connect to the server . Send a simple text message  "HELLO" from the client  to the server and the server to the client and close the connection.

3. Write a program to  create a client that listen to port 12000 using stream sockets .write a simple client program that sends a lower case letters and the server converts into a upper case letters and close the connection.

# Task 4

1. Write a program to create a server that listens to port 54 using stream sockets . Write a simple client program to connect to the server. send multiple text messages from the client to the server .Send multiple text messages from the client to the server and vice-versa. When either party types BYE close the connection

# Task 5

1. Write a program to create a server that listens to port 55 using stream sockets. Write a simple client program to connect to the server. The client should request for a text file and the server should return the file before terminating the connection

# Task 6

1. Write a program to create a server that listens to port 56 using stream sockets. Write a simple client program to connect to the server. Run multiple clients that request the server for binary files. The server should service each client one after the other before terminating the connection

# Task 7

1. Write a program to create a server that listens to port 57 using stream sockets. Write a simple client program to connect to the server. Run multiple clients that request the server for text files. The server should service all clients concurrently.

# Task 8

1. Write a program to create a server that listens to port 59 using datagram sockets. Write a simple client program that requests the server for a binary file. The server should service multiple clients concurrently and send the requested files in response.
