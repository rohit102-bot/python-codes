#message server
import socket

ss=socket.socket()
ss.bind(("localhost",40))
ss.listen(10)
print("message server is running..")
t=ss.accept()
c=t[0]#connection of client socket
b=c.recv(1024)
print(b.decode())
c.send("hello clinet".encode())