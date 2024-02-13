import time
import os

path = '.'  # укажите путь своей директории
path_norm = os.path.normpath(path)

for dirpath, dirnames, filenames in os.walk(path_norm):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.gmtime(filetime))
        filesize = os.path.getsize(filepath)
        parentdir = os.path.dirname(filepath)
        print('*' * 27)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parentdir}')
