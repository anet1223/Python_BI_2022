#!/usr/bin/env python
import argparse
import os, sys

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'Print file content')
parser.add_argument('file',
                    default='',
                    nargs ='*',
                    help = 'Path to file. If empty, stdin is used', 
                    type=str,
                    action='store')

# сохранить аргументы из командной строки в переменную
args = parser.parse_args()


if len(args.file)>0:
    for i in range(len(args.file)):
        if args.file != '':   # проверка, что подан путь к файлу
            if os.path.isfile(args.file[i]):  # проверка, что это файл
                with open(args.file[i]) as file:
                    data = file.read().splitlines() # разделяет на строки
                    for i in data: 
                        print(i)  # выводит результат
            elif os.path.isdir(args.file[i]):  # проверка, что это не папка
                sys.stderr.write('This is directory\n')
            else: # ошибка, если неправильный путь
                sys.stderr.write('No such file or directory\n')
                break
else: # принимает stdin
    data = sys.stdin.read()
    list_data = data.split() # переводит str в list
    for i in list_data:
        print(i)  # печать результатов