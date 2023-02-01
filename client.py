import socket
import threading
from time import sleep

ya_sock = socket.socket()
addr = ("127.0.0.1", 4444)
ya_sock.connect(addr)


def recieving():
    while True:
        data_in = ya_sock.recv(1024).decode()
        print("\n" + data_in)


def sending():
    name = input("Your name: ")
    while True:
        data_out = input()
        if data_out == 'q':
            ya_sock.close()
            break
        data_out2 = name + " :" + data_out
        ya_sock.send(data_out2.encode(encoding='ascii'))


rec_thread = threading.Thread(target=recieving)
rec_thread.start()

send_thread = threading.Thread(target=sending)
send_thread.start()
