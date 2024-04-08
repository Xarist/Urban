import multiprocessing


class WarehouseManager:
    def __init__(self, data):
        self.data = data

    def process_request(self, request):
        product, action, quantity = request

        if action == 'receipt':
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == 'shipment':
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity
            else:
                print(f"Ошибка: не достаточно {product} в наличии.")

    def run(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    data = manager.dict()
    warehouse = WarehouseManager(data)

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    warehouse.run(requests)

    print("Содержимое склада:")
    print(warehouse.data)
