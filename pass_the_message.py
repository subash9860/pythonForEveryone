import itertools
def solution(l):
    l.sort(reverse = True)
    for i in reversed(range(1, len(l)+1)):
        for tup in itertools.combinations(l, i):
            if sum(tup)%3 == 0:
                return int(''.join(map(str,tup)))
    return 0


print(solution([3,1,4,1,5,9]))
