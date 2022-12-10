#!/usr/bin/env python
import argparse
import os

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'List files in the directory')
parser.add_argument('directory', type=str, nargs='?', default='.')
parser.add_argument('--all','-a', action='store_true', 
                    help='Include hiden files in list')

# сохранить аргументы из командной строки в переменную
args = parser.parse_args()

# создать список файлов текущей директории
files = os.listdir(args.directory)

if args.all:
    # добавить текущий и родительский каталоги
    files +=[os.curdir, os.pardir] 
else:
    # убрать файлы, начинающиеся с точки
    files = [idx for idx in files if idx[0] != '.']

# сортировка списка
files.sort()

# печать результата
for file in files:
    print(file)
