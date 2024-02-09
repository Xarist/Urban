my_file = 'file.txt'
with open(my_file, 'r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
print()
print('Файл закрыт') if file.closed==True else print('Файл все еще открыт')
