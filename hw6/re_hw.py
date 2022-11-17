# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:25:49 2022

@author: anja1
"""

import re
import matplotlib.pyplot as plt

raw_list =[]

# считать все куски содержащие "ftp."
with open(r"ref.txt", 'r') as fp:
    for line in fp:
        raw_list.append(re.findall(r'ftp\.[\S]+', line))

# Функция избавляется от вложенных списков
flatten_lambda = lambda lst: (item for sublist in lst for item in sublist)

# Убрать вложенные списки из прочтения
new_list = list(flatten_lambda(raw_list))

# Убрать повторы из прочтения
new_list = [*set(new_list)]

# Разделить строки с ';'
final_list = []

for i in new_list:
    if ';' in i:
        z = i.split(';')
        final_list.append(z)
    else:
        final_list.append([i])

# Убрать вложенные списки
final_list = list(flatten_lambda(final_list))
# Отсортировать список для удобства
final_list.sort()

# Записать ответ в файл
file = open(r"ftps.txt", 'w')
file.writelines('\n'.join(final_list))
file.close()

# списки для работы с текстом A.D.
num = []
word_a = []
sentence = []
word = []

# подсчет чисел, слов с а, предложений с !, слов(без цифр)
with open(r"2430AD.txt", 'r') as fp:
    for line in fp:
        num.append(re.findall(r'[0-9]+.[0-9]*', line))
        word_a.append(re.findall(r'\w*[aA]\w*', line))
        sentence.append(re.findall(r"(\w[^.?]*?\!)", line))
        word.append(re.findall(r'\b[a-zA-Z]+\b', line))


# Убрать вложенные списки
numbers = list(flatten_lambda(num))
print(numbers)
words_with_a = list(flatten_lambda(word_a))
print(words_with_a)
sentences = list(flatten_lambda(sentence))
print(sentences)
words = list(flatten_lambda(word))

# Перевести все слова в нижний регист
words_lower = list(map(lambda x: x.lower(), words))

# Отобрать уникальные слова
words_unique = [*set(words_lower)]

# Посчитать длину слов
words_length = []

for i in words_unique:
    words_length.append(len(i))

words_length.sort()

# Сделать словарь из длины слов и их количества
dic_length = dict((x,words_length.count(x)) for x in set(words_length))

# Посчитать долю
part = []
for i in dic_length.values():
    part.append(i/len(words_unique))

# Построить график
plt.bar(list(dic_length.keys()), part, color='g')
plt.xlabel('Length of the word')
plt.ylabel('Part of unique words with such length')
plt.show()

# Функция перевода на кирпичный язык
def translate(text):
    dic_brick = {'е':'еКЕ','Е':'еКЕ',
                 'ы':'ыКЫ','Ы':'ыКЫ',
                 'а':'аКА', 'А':'аКА',
                 'о':'оКО','О':'оКО',
                 'я':'яКЯ','Я':'яКЯ',
                 'и':'иКИ','И':'иКИ',
                 'у':'уКУ','У':'уКУ',
                 'э':'эКЭ','Э':'эКЭ',
                 'ё':'ёКЁ','Ё':'ёКЁ',
                 'ю':'юКЮ','Ю':'юКЮ'}
    tbl = text.maketrans(dic_brick)
    print(text.translate(tbl))

# Функция нахождения предложения с заданным количеством слов
def sentence_finder (text,n):
    sentences = re.findall(r"(\w[^.?]*?[!.?])", text)
    new_list = []

    for i in sentences:
        m = tuple(re.findall(r"\b\w+\b", i))
        if len(m) == n:
            new_list.append(m)
    print(new_list)
