import array as arr

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0,n):
        a = int(input())
        numbers = arr.array(a)

        numbers.append(4)
    print(numbers)
    #     a[i] = int(input())
    # for i in range(0,n):
    #     print(lst)