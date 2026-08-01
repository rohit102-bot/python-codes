import socket
s=socket.socket(type=socket.SOCK_DGRAM)
s.bind(("localhost",40))
msg="hello"
s.sendto(msg.encode(),("localhost",30))
while True:
    t=s.recvfrom(1024)
    print(t[0].decode())
    break
