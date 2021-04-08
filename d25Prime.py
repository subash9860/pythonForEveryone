# Task
# A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

# Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

# Input Format

# The first line contains an integer, , the number of test cases.
# Each of the  subsequent lines contains an integer, , to be tested for primality.

# Constraints

# Output Format

# For each test case, print whether  is  or  on a new line.

# Sample Input

# 3
# 12
# 5
# 7
# Sample Output

# Not prime
# Prime
# Prime
# Explanation

# Test Case 0: .
#  is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

# Test Case 1: .
#  is only divisible  and itself, so we print  on a new line.

# Test Case 2: .
#  is only divisible  and itself, so we print  on a new line.
# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt
from sys import stdin


def checkPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
for line in stdin:
    val = int(line)
    if (val >= 2 and checkPrime(val)):
        print("Prime")
    else:
        print("Not prime")
