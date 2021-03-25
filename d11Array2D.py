# Context
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

# Example

# In the array shown above, the maximum hourglass sum is  for the hourglass in the top left corner.

# Input Format

# There are  lines of input, where each line contains  space-separated integers that describe the 2D Array .

# Constraints

# Output Format

# Print the maximum hourglass sum in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

#  contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum () is:

# 2 4 4
#   2
# 1 2 4

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

 
 
#This function will return the sum of the hourglass
def sum_hg(x, y):
    sum = arr[x][y] + arr[x][y+1] +arr[x][y+2]
    sum = sum + arr[x+1][y+1]
    sum = sum + arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
    return sum
 
size = len(arr)
sum = -63
 
for x in range(0, (size-2)):
    for y in range(0, (size-2)):
        k = sum_hg(x, y)
        if k > sum:
            sum = k
 
print(sum)
