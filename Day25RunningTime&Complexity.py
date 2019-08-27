# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
T=int(input())


for i in range(T):
    n = int(input())
    if n == 3:
        print("Prime")
    elif n == 1:
        print("Not prime")
    elif n % 2 == 0:
        print("Not prime")
    else:
        f = 0
        for i in range(3, int(math.sqrt(n)) + 1, + 2):
            if n % i == 0:
                f = 1
                print("Not prime")
                break
        if f == 0:
            print("Prime")
