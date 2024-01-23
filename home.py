class House:
    def __init__(self, numberOfFloors=10):
        self.numberOfFloors = numberOfFloors

    def printFloors(self):
        for floor in range(1, self.numberOfFloors + 1):
            print("Текущий этаж равен", floor)


myHouse = House()

myHouse.printFloors()
