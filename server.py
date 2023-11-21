# server.py

import socket
import threading

host = socket.gethostname()  
ip = socket.gethostbyname(host)

print('Server IP:', ip)

port = int(input('Enter port number: '))  

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

print('Server started on IP:', ip, 'Port:', port)

client_addr = None

def receive():
    global client_addr
    while True:
        msg, addr = server.recvfrom(1024)
        client_addr = addr
        print('Received from', addr, ":", msg.decode())
        
def write():
    while True:
        msg = input('Enter message: ')
        server.sendto(msg.encode(), client_addr)
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()