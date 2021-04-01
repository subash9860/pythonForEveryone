# Task
# Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
# A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the  instance variable.
# Input Format

# You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in  lines of input. The first line contains , the size of the elements array. The second line has  space-separated integers that describe the  array.

# Constraints

# , where 
# Output Format

# You are not responsible for printing any output; the Solution class will print the value of the  instance variable.

# Sample Input

# STDIN   Function
# -----   --------
# 3       __elements[] size N = 3
# 1 2 5   __elements = [1, 2, 5]
# Sample Output

# 4
# Explanation

# The scope of the  array and  integer is the entire class instance. The class constructor saves the argument passed to the constructor as the  instance variable (where the computeDifference method can access it).

# To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any  elements: 


# The maximum of these differences is , so it saves the value  as the  instance variable. The locked stub code in the editor then prints the value stored as , which is .

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.maximumDifference = max_element - min_element


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
