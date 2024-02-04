class Vehicle():
    def __init__(self):
        self.vehicle_type = None


class Car():
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1200000
        self.vehicle_type = 'Sedan'

    def horse_powers(self):
        return 250


almera = Nissan()
print(almera.vehicle_type)
print(almera.price)
print(almera.horse_powers())
