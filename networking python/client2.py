
import socket
ss=socket.socket()
ss.connect(("localhost",40))
ss.send("hello server".encode())
b=ss.recv(1024)
print(b.decode())