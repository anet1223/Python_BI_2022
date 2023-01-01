#!/usr/bin/env python
import argparse
import os, sys

# взять аргументы из командной строки
parser = argparse.ArgumentParser(description = 'Delete file or directory')
parser.add_argument('file',
                    default='',
                    help = 'Path to file or directory', 
                    type=str,
                    action='store')

parser.add_argument('-r',
                    default=False,
                    help = 'Remove directory', 
                    action='store_true')

# сохранить аргументы из командной строки в переменную
args = parser.parse_args()

if os.path.isfile(args.file):
    # если файл, то удалить
    os.remove(args.file)
    print("% s removed successfully" % args.file)
elif os.path.isdir(args.file) and args.r == False:
    # если папка и не поставлен флаг '-r', не удалять
    print("rm: cannot remove %s it is a directory" % args.file)
elif os.path.isdir(args.file) and args.r == True:
    # если папка и флаг, удалить папку
    os.rmdir(args.file)
    print("% s removed successfully" % args.file)   
else:
    # если неправильное имя, написать ошибку
    sys.stderr.write('No such file or directory\n')
    
