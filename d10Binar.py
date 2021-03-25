# Task
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

# Example

# The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

# Input Format

# A single integer, .

# Constraints

# Output Format

# Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2
# Explanation

# Sample Case 1:
# The binary representation of  is , so the maximum number of consecutive 's is .

# Sample Case 2:
# The binary representation of  is , so the maximum number of consecutive 's is .

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n=str(bin(int(input())))
    n=n[2:]
    maxmum=0
    i=0
    c=0
    while i<(len(n)):
        if n[i]=="1":
            c=c+1
        else:
            c=0
        if c>maxmum:
            maxmum=c
        i+=1   
    print(maxmum)
