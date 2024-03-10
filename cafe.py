import threading
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.tables = [Table(number) for number in tables]
        self.queue = Queue()

    def customer_arrival(self, customer_number):
        print(f"Посетитель номер {customer_number} прибыл.", flush=True)

        for table in self.tables:
            if not table.is_busy:
                self.serve_customer(customer_number, table)
                return

        self.queue.put(customer_number)
        print(f"Посетитель номер {customer_number} добавлен в очередь ожидания.", flush=True)

    def serve_customer(self, customer_number, current_table):
        current_table.is_busy = True
        print(f"Посетитель номер {customer_number} занимает стол {current_table.number}.", flush=True)
        time.sleep(5)  # время обслуживания
        current_table.is_busy = False
        print(f"Посетитель номер {customer_number} закончил и ушёл.", flush=True)

        if not self.queue.empty():
            next_customer = self.queue.get()
            for table in self.tables:
                if not table.is_busy:
                    self.serve_customer(next_customer, table)
                    return


class Customer(threading.Thread):
    def __init__(self, cafe, customer_number):
        super().__init__()
        self.cafe = cafe
        self.customer_number = customer_number

    def run(self):
        self.cafe.customer_arrival(self.customer_number)


tables = [1, 2, 3]  # список номеров столов
cafe = Cafe(tables)

for i in range(10):  # количество посетителей
    customer = Customer(cafe, i + 1)
    customer.start()
