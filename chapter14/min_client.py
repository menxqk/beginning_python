import socket

s = socket.socket()
s.connect(('127.0.0.1', 9090))
print(s.recv(1024).decode())
