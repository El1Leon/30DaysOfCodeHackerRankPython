import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())  # Number of rows
    gmail_users = []  # List to store first names of Gmail users
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()  # Read input line
        firstName = first_multiple_input[0]  # First name
        emailID = first_multiple_input[1]  # Email ID

        # Check if the email ends with "@gmail.com"
        if emailID.endswith("@gmail.com"):
            gmail_users.append(firstName)  # Add first name to the list

    # Sort the list of Gmail users alphabetically
    gmail_users.sort()

    # Print each Gmail user's first name
    for name in gmail_users:
        print(name)