# MathServer/CalcServer
import socket

ss=socket.socket()
ss.bind(("localhost",40))
ss.listen(5)
print("Math Server is Running ")
while True:
    t=ss.accept()
    c=t[0]
    b=c.recv(2048)
    expr=b.decode()
    res=eval(expr)
    result=f'Result is {res}'
    c.send(result.encode())
    print("result sent")
    ss.close()
    break