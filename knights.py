from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        # Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        print(f'{self.name}, на нас напали!', flush=True)
        count = 0
        enimies = 100
        while enimies != 0:
            count += 1
            enimies -= self.skill
            print(f'{self.name} сражается {count} день(дня)... Осталось {enimies} врагов', flush=True)
            # sleep(1)
        print(f'{self.name} одержал победу за {count} дней(дня)!', flush=True)


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')
