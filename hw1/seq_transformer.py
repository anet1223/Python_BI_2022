# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:39:56 2022

@author: anja1

Программа, которая в бесконечном цикле считывает команды от
пользователя. После команды программа запрашивает у пользователя
последовательность нуклеиновой кислоты и распечатывает результат.

Список команд:
    exit — завершение исполнения программы
    transcribe — напечатать транскрибированную последовательность
    reverse — напечатать перевёрнутую последовательность
    complement — напечатать комплементарную последовательность
    reverse complement — напечатать обратную комплементарную последовательность



"""

# Словари для транскибции и комплиментации
dic_tr = {'A':'U','T':'A','G':'C', 'C':'G',
          'a':'u','t':'a','g':'c','c':'g'}

dic_com_DNA = {'A':'T','T':'A','G':'C', 'C':'G',
               'a':'t','t':'a','g':'c','c':'g'}

dic_com_RNA = {'A':'U','U':'A','G':'C', 'C':'G',
               'a':'u','u':'a','g':'c','c':'g'}

# Список разрешенных символов на вхождение
allow = ['a','u','t','g','c','A','T','G','C','U']

# Функции для работы команд
def reverse(seq):
    print(seq[::-1])

def transcribe(seq):
    tbl = seq.maketrans(dic_tr)
    print(seq.translate(tbl))
    
def complement(seq):
    if 'u' in seq.lower():
        tbl = seq.maketrans(dic_com_RNA)
    else:
        tbl = seq.maketrans(dic_com_DNA)
    print(seq.translate(tbl))
    
def rev_complement(seq):
    if 'u' in seq.lower():
        tbl = seq.maketrans(dic_com_RNA)
    else:
        tbl = seq.maketrans(dic_com_DNA)
    print(seq.translate(tbl)[::-1])

# Бесконечный цикл для работы программы
while 0 == 0:
    
    # Ввод команды пользователем
    command = input('Enter command:')
    
    # Выход из программы при команде 'Exit'
    if command == 'exit':
        print('Good luck!')
        break
    
    # Ввод последовательности пользователем
    seq = input('Enter sequence:')
    
    # Переменные для проверяющего цикла
    a = 0
    b = 0
    c = 0
    
    # Проверка корректности последовательности
    while a == 0 or b == 0 or c == 0:
        # Проверка на наличие недопустимых символов
        for i in seq:
            if i not in allow:
               print('Invalid symbol. Please, try again')
               seq = input('Enter sequence:')
               a = 0
               break
            else:
               a = 1
        # Проверка на недопустимое сочетание 'T' и 'U'
        if 't' in seq.lower() and 'u' in seq.lower():
            print('Invalid conbination. Please, try again')
            seq = input('Enter sequence:')
            b = 0
            continue
        else:
            b = 1
    
        # Проверка на РНК транскрибцию
        if 'u' in seq.lower() and command == 'transcribe':
            print('Invalid command for RNA. Please, try DNA sequence')
            seq = input('Enter sequence:')
            c = 0
            continue
        else:
            c = 1
    
    
    # Выполнение функции в соответствии с введенной командой
    if command == 'reverse':
        reverse(seq)
    elif command == 'transcribe':
        transcribe(seq)
    elif command == 'complement':
        complement(seq)
    elif command == 'reverse complement':
        rev_complement(seq)
    else:
        print('Unknown command. Please, try again.')


