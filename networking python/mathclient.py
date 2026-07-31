# Math client

import socket

s=socket.socket()
s.connect(("localhost",40))
expr=input("Enter Expression :")
s.send(expr.encode())
b=s.recv(2048)
print(b.decode())
