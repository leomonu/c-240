import socket
from threading import Thread
ip_address="127.0.0.1"
port=5000
server=None
clients={}

def accept_connections():
    global server
    global clients
    while True:
        client,address=server.accept()
        print(client,address)

def setup():
    global port
    global ip_address
    global server

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((ip_address,port))
    server.listen(100)
    print("Server is waiting for incoming connection")
    accept_connections()

setup_thread=Thread(target=setup())
setup_thread.start()