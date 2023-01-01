#!/usr/bin/env python
import argparse
import sys, os

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'Count lines, words or bytes')
parser.add_argument('-l', '--lines', 
                    help = 'Count number of lines', 
                    default = False, 
                    action = 'store_true')
parser.add_argument('-w', '--words',
                    dest = 'words', 
                    help = 'Count number of words', 
                    default = False,
                    action = 'store_true')
parser.add_argument('-c', '--bytes', 
                    help = 'Count number of bytes', 
                    default = False,
                    action = 'store_true')
parser.add_argument('file',
                    default='',
                    nargs ='*',
                    help = 'Path to file. If empty, stdin is used', 
                    type=str,
                    action='store')
# сохранить аргументы из командной строки в переменную
args = parser.parse_args()

# функция для подсчета строк и слов
def data_count(data):
    lines = data.count('\n')
    words = len(data.split())
    return lines, words

# функция для печати результатов
def print_result(args, lines, words, byte):
    if args.lines:
        print(lines,'',end='')
    if args.words:
        print(words,'',end='')
    if args.bytes:
        print(byte,'',end='')
    if args.file == '':
        print('')
    else:
        print(args.file[0]) 
       
if args.file != '':   # проверка, что подан путь к файлу
    if os.path.isfile(args.file[0]):  # проверка, что это файл
        with open(args.file[0]) as file:
            data = file.read()
            lines, words = data_count(data)
        with open(args.file[0], 'rb') as file: 
            # открытие в бинарном режиме для подсчета байтов
            data = file.read()
            byte = len(data)
            print_result(args, lines, words, byte)
    elif os.path.isdir(args.file[0]):  # проверка, что это не папка
        sys.stderr.write('This is directory\n')
    else: # ошибка, если неправильный путь
        sys.stderr.write('No such file or directory\n')
else: # принимает stdin
    data = sys.stdin.read()
    lines, words = data_count(data)
    byte = len(bytes(data,'utf-8'))
    print_result(args, lines, words, byte)