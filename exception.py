def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'Возникла ошибка: невозможно преобразовать {s} в целое число'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Возникла ошибка: файл {filename} не найден'
    except IOError:
        return f'Возникла ошибка: ошибка ввода/вывода при работе с {filename}'


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return 'Возникла ошибка: Нельзя делить на 0'
    except TypeError:
        return 'Возникла ошибка: аргументы должны быть числами'


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'Возникла ошибка: индекс {index} вне диапозона'
    except TypeError:
        return 'Возникла ошибка: индекс должен быть целым числом'
