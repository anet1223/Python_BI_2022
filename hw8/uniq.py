#!/usr/bin/env python
import argparse
import os, sys

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'Omit repeat lines')
parser.add_argument('file',
                    default='',
                    nargs ='*',
                    help = 'Path to file. If empty, stdin is used', 
                    type=str,
                    action='store')

# сохранить аргументы из командной строки в переменную
args = parser.parse_args()

# функция для отбора уникальных значений
def get_unique(data):
    unique = []

    for i in data:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique


if args.file != '':   # проверка, что подан путь к файлу
    if os.path.isfile(args.file[0]):  # проверка, что это файл
        with open(args.file[0]) as file:
            data = file.read().splitlines() # разделяет на строки
            unique_data = get_unique(data) # отбирает уникальные значения
            for i in unique_data: 
                print(i)  # выводит результат
    elif os.path.isdir(args.file[0]):  # проверка, что это не папка
        sys.stderr.write('This is directory\n')
    else: # ошибка, если неправильный путь
        sys.stderr.write('No such file or directory\n')
else: # принимает stdin
    data = sys.stdin.read()
    list_data = data.split() # переводит str в list
    unique_data = get_unique(list_data) # отбирает уникальные значения
    for i in unique_data:
        print(i)  # печать результатов