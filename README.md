# LocalChatUDP

This repository contains the code for a simple UDP-based chat application implemented in Python. The project is divided into two main components: client.py and server.py.

### Features
- [x] Server Script (server.py): Sets up a UDP server that listens for incoming messages from clients, displays them, and allows the server operator to respond. The server displays the IP and port number on startup for clients to connect.

- [x] Client Script (client.py): Connects to the UDP server using the provided server IP and port number. It allows users to send and receive messages in real-time.

### How to Use
Start the Server:

Run python server.py and enter the desired port number when prompted.
Note the server IP and port displayed on startup.

Connect with Client:
Run python client.py, enter the server IP and port number when prompted, and start chatting.
Objective
The main objective of this project is to demonstrate the basic implementation of a chat application using Python's socket programming capabilities with UDP protocol, which offers simplicity and speed for real-time message exchanges.

The chat is performed between a client and a server.

The server will first start-up and make the user choose a port number. Then the server prints out its IP address and port number.

The client then will start up and create a socket based on the information (IP address and port number) provided by the server.

The client/server is able to communicate with each other in a continuous manner.

###### Coded for a Computer Networking Class

