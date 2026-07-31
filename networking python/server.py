import socket
s=socket.socket()
s.bind(("localhost",50))
s.listen(5)
print("server is running ....")
s.accept()
print("connection established...")
s.close()