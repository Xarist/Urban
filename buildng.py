class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False


building1 = Building(9, 'жилой дом')
building2 = Building(9, 'жилой дом')
building3 = Building(3, 'офис')
print(building1 == building2)
print(building2 == building3)
