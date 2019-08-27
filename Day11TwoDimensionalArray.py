#Version 1

#!/bin/python3

import sys

def getHourglassSum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]    
    sum += matrix[row+1][col]    
    sum += matrix[row+1][col-1]    
    sum += matrix[row+1][col+1]
    return sum   

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(" ")]
    arr.append(arr_t)


maxHourglassSum = -63
for i in range(1,5):
    for j in range(1,5):
        currentHourglassSum = getHourglassSum(arr, i, j)
        if currentHourglassSum > maxHourglassSum:
            maxHourglassSum = currentHourglassSum

print(maxHourglassSum)