# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    #In the 3-way partition, only the part with the elements less than the pivot 
    #and the part with the elements greater than the pivot need to be sorted.
    x = a[l]
    j = i = l
    k = r

    while i <= k:
        if a[i] < x:
            a[i] , a[j] = a[j], a[i]
            j += 1
            i += 1

        elif a[i] == x:
            i += 1   

        else:
            a[i], a[k] = a[k], a[i]
            k -= 1

    return j, k

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    j, k = partition3(a, l, r)
    randomized_quick_sort(a, l, j - 1) #m1 - 1
    randomized_quick_sort(a, k + 1, r) #m2 + 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')