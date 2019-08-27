#!/bin/python3

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
isSorted = False

while not isSorted:
    isSorted = True
    i = 0
    for i in range(0, len(a)):
        if i < len(a) - 1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                isSorted = False
                swaps += 1

print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))