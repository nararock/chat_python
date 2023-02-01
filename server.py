import socket
from _thread import start_new_thread
import threading


def threaded(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            print('Bye')
            break
        for i in conn_list:
            if (i != c):
                i.send(data.encode())


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 4444  # Port to listen on (non-privileged ports are > 1023)
conn_list = list()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    conn_list.append(conn)
    t = threading.Thread(target=threaded, args=(conn,))
    t.start()

for c in conn_list:
    c.close()
