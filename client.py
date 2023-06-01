import socket
from threading import Thread
ip_address="127.0.0.1"
port=5000
server=None

buffersize=4096

def setup():
    global port
    global ip_address
    global server

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.connect((ip_address,port))
setup()
   