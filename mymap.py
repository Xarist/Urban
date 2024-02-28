def seq(x):
    return x ** 2


def odd(x):
    return x % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

print(list(map(seq, filter(odd, my_list))))

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, my_list))))
