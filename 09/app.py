import os

file_path = '/home/filedir/text.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f'Файл {file_path} не найден.')
except Exception as e:
    print(f'Произошла ошибка при чтении файла: {e}')