def draw(ch):
    def drawLine(n):
        print(ch*n)
    return drawLine

drawstars=draw("*")
drawdollars=draw("$")
drawstars(10)