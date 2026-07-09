def drawLine(ch="*",length=40):
    for i in range(length):
        print(ch,end='')
    print()

drawLine()
drawLine("$")
drawLine(length=20)
drawLine("^",50)