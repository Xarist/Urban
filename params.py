def print_params(a=1, b='строка', c=True):
    print(a)
    print(b)
    print(c)


print_params()
print_params(2)
print_params(3, c=False)
print_params(4, 'stroka', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = (2, 3.14, True)
values_dict = {'a': 2, 'b': 'stroka', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [542, 'Hello!']
print_params(*values_list_2, 42)
