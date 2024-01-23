class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for i in range(40):
    new_building = Building()
    print(f"Объект № {Building.total}")


print(f"Всего создано объектов: {Building.total}")