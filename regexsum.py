# In this assignment you will read through and parse 
# a file with text and numbers. You will extract all 
# the numbers in the file and compute the sum of the numbers.

import re
# fname = input('Enter file name:')
fh = open('regex_sum_1166282.txt')
lst = list()
for line in fh:
    y = re.findall('[0-9]+',line)
    lst+=y
    
sum = 0
for z in lst:
    sum += int(z)
    
print(sum)