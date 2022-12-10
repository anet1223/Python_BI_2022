#!/usr/bin/env python
import argparse
import os, sys

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'Print last lines of the file')
parser.add_argument('n',
                    default=10,
                    help = 'number of lines to return', 
                    type=int,
                    action='store')
parser.add_argument('file',
                    default='',
                    nargs ='*',
                    help = 'Path to file. If empty, stdin is used', 
                    type=str,
                    action='store')


# сохранить аргументы из командной строки в переменную
args = parser.parse_args()

# задание количества строчек
if args.n == None:
    n = 10
else:
    n = abs(args.n)

if len(args.file)>0:
    for i in range(len(args.file)):
        if args.file != '':   # проверка, что подан путь к файлу
            if os.path.isfile(args.file[i]):  # проверка, что это файл
                with open(args.file[i]) as file:
                    data = file.read().splitlines() # разделяет на строки
                    stop = len(data)
                    start = stop - n
                    for i in data[start:stop]: 
                        print(i)  # выводит результат
            elif os.path.isdir(args.file[i]):  # проверка, что это не папка
                sys.stderr.write('This is directory\n')
            else: # ошибка, если неправильный путь
                sys.stderr.write('No such file or directory\n')
                break
else: # принимает stdin
    data = sys.stdin.read()
    list_data = data.split() # переводит str в list
    stop = len(list_data)
    start = stop - n
    for i in list_data[start:stop]:
        print(i)  # печать результатов