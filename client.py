# client.py

import socket
import threading 

ip = input('Enter server IP: ')
port = int(input('Enter port number: '))  

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive():
    while True:
        msg, addr = client.recvfrom(1024)
        print('Received from server:', msg.decode())

def write():
    while True:
        msg = input('Enter message: ')
        client.sendto(msg.encode(), (ip, port))
        
receive_thread = threading.Thread(target=receive) 
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()