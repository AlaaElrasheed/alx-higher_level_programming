#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    list1 = []
    matrix1 = []
    for i in matrix[:]:
        list1 = i.copy()
        for j in range(len(list1)):
            list1[j] *= list1[j]
        matrix1.append(list1)
    return matrix1
