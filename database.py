class DataBase:
    def __init__(self):
        self.spot_motorcycle = []
        self.spot_van = []
        self.spot_car = []

    def addMotorcycle(self, motorcycle):
        self.spot_motorcycle.append(motorcycle)

    def addCar(self, car):
        self.spot_car.append(car)

    def addVan(self, van):
        self.spot_van.append(van)

    def printMotorcycles(self):
        print(self.spot_motorcycle)

    def printCars(self):
        print(self.spot_car)

    def printVans(self):
        print(self.spot_van)



class Vehicle:
    def __init__(self, type , spot_size):
        self.type = type
        self.spot_size = spot_size


class MotorCycle(Vehicle):
    def __init__(self, spot_size):
        Vehicle.__init__(self,'motorcycle',spot_size)


class Car(Vehicle):
    def __init__(self, spot_size):
        Vehicle.__init__(self, 'car', spot_size)

class Van(Vehicle):
    def __init__(self, spot_size):
        Vehicle.__init__(self,'van', spot_size)

car1 = Car('medium')

def main():
    database = DataBase()
    car1 = Car('medium')
    car2 = Car('large')
    mot1 = MotorCycle('small')
    van1 = Van('large')

    database.addCar(car1)
    database.addCar(car2)
    database.addMotorcycle(mot1)
    database.addVan(van1)

    database.printCars()
    database.printMotorcycles()
    database.printVans()

main()
