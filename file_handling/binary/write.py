with open("file1.dat","wb") as f:
          b=bytes([65,66,67,68,69,70])
          f.write(b)
          print("data written inside file")