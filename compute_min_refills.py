# python3
import sys


def compute_min_refills(d, m, n, stops):
    # write your code here 
    numRefills = 0 
    currentRefill = 0

    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and 
               stops[currentRefill + 1] - stops[lastRefill] <= m):
            currentRefill += 1


    if lastRefill == currentRefill:
        return -1
        
    if currentRefill <= n:
        numRefills += 1  


    return numRefills   
                     

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops =  [int(x) for x in input().split()]
    assert (len(stops) == n)
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))