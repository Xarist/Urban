class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i > self.end:
            raise StopIteration()
        else:
            if self.i % 2 != 0:
                self.i += 1
            result = self.i
            self.i += 2
            return result


even_nums = EvenNumbers(10,25)

for i in even_nums:
    print(i)
