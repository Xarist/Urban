# Динамическое определение функций
print(f'{"Динамическое определение функций":*^40}')


def my_func_def(x):
    if x % 2 == 0:
        def mult(n):
            return x * n

        return mult
    else:
        def div(n):
            return x / n

        return div


my_func_oper = my_func_def(65)
print(my_func_oper(5))

# Лямбда функции
print(f'{"Лямбда функции":*^40}')
my_list = [1, 2, 3, 4, 5, 6]
print(*list(map(lambda x: x ** 2, my_list)))


def my_func_map(n):
    return n ** 2


print(*list(map(my_func_map, my_list)))

# Вызываемые объекты
print(f'{"Вызываемые объекты":*^40}')


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect = Rect(4, 5)
print(rect())
