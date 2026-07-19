class Engine:
    def start(self):
        print("engine start.....")
    def stop(self):
        print("engine stop")

class Car:
    def __init__(self):
        self.e=Engine()
    def carStart(self):
        self.e.start()
    def carStop(self):
        self.e.stop()

audi=Car()
audi.carStart()
audi.carStop()