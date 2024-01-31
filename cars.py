class Car:
    price = 1000000

    def horse_powers(self):
        return 0


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return 200


class Kia(Car):
    price = 1250000

    def horse_powers(self):
        return 150

ceed = Kia()
print(ceed.price)
print(ceed.horse_powers())

patrol = Nissan()
print(patrol.price)
print(patrol.horse_powers())