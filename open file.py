file_name = 'file.txt'
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
print(file_content)