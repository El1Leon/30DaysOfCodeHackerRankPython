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


# #Version 2

# #!/bin/python3

# import sys
# arr = []
# def max(a,b):
#     return a if a>b else b
# def sum(i,j):
#     return arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
# ans = -100
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)
# for i in range(4):
#     for j in range(4):
#         ans = max(ans,sum(i,j))
# print(ans)

