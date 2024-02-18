import warnings


def division(a, b):
    try:
        if abs(b) < 0.01:
            warnings.warn('Делитель близок к 0!', UserWarning)
    except UserWarning as war:
        print(f'Предупреждение было перехвачено как исключение: {war}')
    return a/b


print('Фильтр установлен в "always"')
warnings.simplefilter("always")
print(division(6, 0.001))
print('\n')

print('Фильтр установлен в "ignore"')
warnings.simplefilter("ignore")
print(division(6, 0.001))
print()

print('Фильтр установлен в "error"')
warnings.simplefilter("error")
print(division(6, 0.001))
print()
