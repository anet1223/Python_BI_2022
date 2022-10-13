# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:41:26 2022

@author: anja1
"""
# Импорт модулей для работы путей к файлам
import os
import glob

# Функция для подсчета GC
def GC_count(line):
    count = 0
    for i in line.lower():
        if i == 'g' or i == 'c':
            count += 1  
    return round(count/len(line)*100,1)

# Функция для подсчета среднего качества
def mean_ql(line):
    q_num =[]
    for i in line:
        q_num.append(ord(i)-33)
    return(round(sum(q_num)/len(q_num),1))

# Фильтр для GC
def filter_GC(line, start, stop):
    if GC_count(line) >= start and GC_count(line) <= stop:
        return True
    else:
        return False

# Фильтр для качества
def filter_ql(line, threshold):
    if mean_ql(line) >= threshold:
        return True
    else:
        return False    

# Фильтр для длины    
def filter_length(line, fr, to):
    if len(line) >= fr and len(line) <= to:
        return True
    else:
        return False

# Основная функция
def main(input_fastq, output_file_prefix, gc_bounds = (0,100), length_bounds = (0,2**32), quality_threshold = 0, save_filtered = False):
    
    # input_fastq - вводится путь к папке, где лежит fastq файл. 
    # Если их в папке несколько, берется первый.
    # Для Windows путь “C:\\xyz\\Documents\\My all docs”
    # Для Linux/Unix путь “/Documents/Myfolder”
    
    os.chdir(input_fastq)
    f = open(glob.glob('*.fastq')[0])
    f1 = f.read().splitlines() 

    # Если сохраняем файлы, вводим название в output_file_prefix
    # Пример: output_file_prefix = 'new'
    if save_filtered == True:
        f_pass = open(output_file_prefix + "_passed.fastq","w+")
        f_fail = open(output_file_prefix + "_failed.fastq","w+")

    # Проверка две ли цифры в gc_bounds    
    if type(gc_bounds)==int:
        gc_bounds = (0,gc_bounds)
    
    # Итерация по каждой второй линии
    for line in f1[1::4]:
        # Проверка всех фильтров
        if filter_length(line,fr = length_bounds[0], to = length_bounds[1]) == True and filter_GC(
                line,start = gc_bounds[0], stop = gc_bounds[1]) == True and filter_ql(
                    f1[(f1.index(line))+2], threshold = quality_threshold):
        # Запись отобранных ридов
            f_pass.write(f1[(f1.index(line)-1)])
            f_pass.write("\n")
            f_pass.write(f1[(f1.index(line))])
            f_pass.write("\n")
            f_pass.write(f1[(f1.index(line)+1)])
            f_pass.write("\n")
            f_pass.write(f1[(f1.index(line))+2])
            f_pass.write("\n")
        else:
        # Запись неотобранных ридов
            f_fail.write(f1[(f1.index(line)-1)])
            f_fail.write("\n")
            f_fail.write(f1[(f1.index(line))])
            f_fail.write("\n")
            f_fail.write(f1[(f1.index(line)+1)])
            f_fail.write("\n")
            f_fail.write(f1[(f1.index(line)+2)])
            f_fail.write("\n")
    # Закрытие файлов
    f.close()
    if save_filtered == True:
        f_pass.close()
        f_fail.close()
    
    
