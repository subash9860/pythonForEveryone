import math
def solution(area):
    list_of_sqr = []
    while area !=0:
        n = int(math.sqrt(area))
        list_of_sqr.append(n*n)
        area = area - n*n
    return list_of_sqr

print(solution(12))