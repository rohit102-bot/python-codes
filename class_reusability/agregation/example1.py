class Engine:
    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")


class Car:
    def __init__(self, engine):
        self.engine = engine      # Aggregation

    def carStart(self):
        self.engine.start()

    def carStop(self):
        self.engine.stop()


# Engine exists independently
e1 = Engine()

# Pass the existing engine to the car
audi = Car(e1)

audi.carStart()
audi.carStop()