#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N: The maximum integer to consider
#  2. INTEGER K: The limit for the bitwise AND result
#

def bitwiseAnd(N, K):
    # Initialize the maximum value of A & B that is less than K
    max_and = 0
    
    # Iterate over all pairs (A, B) where 1 <= A < B <= N
    for A in range(1, N):
        for B in range(A + 1, N + 1):
            # Calculate the bitwise AND of A and B
            current_and = A & B
            
            # Check if the current AND result is less than K
            # and update max_and if it is the highest so far
            if current_and < K:
                max_and = max(max_and, current_and)
            
            # Early exit if we find the maximum possible value (K-1)
            # This is because K-1 is the highest value A & B can reach while being less than K
            if max_and == K - 1:
                return max_and

    # Return the maximum found bitwise AND that is less than K
    return max_and

if __name__ == '__main__':
    # Open the output file to write the results
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input().strip())

    # Iterate over each test case
    for t_itr in range(t):
        # Read N and K from the input for the current test case
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])  # N is the maximum integer to consider
        lim = int(first_multiple_input[1])    # K is the limit for the AND result

        # Call the bitwiseAnd function to calculate the result for the current test case
        res = bitwiseAnd(count, lim)

        # Write the result to the output file
        fptr.write(str(res) + '\n')

    # Close the output file
    fptr.close()
