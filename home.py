class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Количество этажей:", self.numberOfFloors)


# Создаем экземпляр класса House
myHouse = House()

# Изменяем количество этажей и выводим в консоль
myHouse.setNewNumberOfFloors(5)