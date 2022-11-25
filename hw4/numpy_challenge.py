# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:41:06 2022

@author: anja1
"""
import numpy as np

# Перемножение матриц
def matrix_multiplication(a,b):
    return np.matmul(a,b)

# Проверка возможности перемножения матриц
def multiplication_check(l):
    for arr in range(1,len(l)):
        first_arr = l[arr-1].shape
        second_arr = l[arr].shape
        if first_arr[1] != second_arr[0]:
            answer = False
        else:
            answer = True
    return answer

# Перемножение списка матриц, при возможности    
def multiply_matrices(l):
    if multiplication_check(l) == True:
        result = l[0]
        for arr in range(1,len(l)):
            result = matrix_multiplication(result, l[arr])
        return result
    else:
        return None

# Рассчет расстояния между точками            
def compute_2d_distance(a,b):
    distance = a - b
    return np.sqrt((distance[0])**2 + (distance[1])**2) 

# Вычисление расстояния между любым количеством значений
def compute_multidimensional_distance(a,b):
    distance = a - b
    result = 0
    for i in range(len(a)):
        result +=(distance[i])**2
    return np.sqrt(result)

# Рассчет матрицу попарных расстояний между строками и колонками
def compute_pair_distances(a):
    arr =  np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            arr[i][j] = compute_multidimensional_distance(a[i],a[j])
            arr[j][i] = arr [i][j]            
    return arr

if __name__ == "__main__":
    # Cоздание трех массивов разными способами
    arr1 = np.array([13, 23, 34, 45, 56, 67, 78, 89, 100])
    arr2 = np.arange(12).reshape(3, 4)
    arr3 = np.random.randint(0, 15, size = (4, 6))