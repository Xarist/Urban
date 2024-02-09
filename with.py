my_file = 'file.txt'
with open(my_file, 'r') as file:
    for line in file:
        print(line, end='')