# Uses python3
import sys
from math import inf

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    #create a new list from 0 to m + 1(not including the m + 1 term) in the list 
    min_num_coins = [None] * (m + 1)
    #min_num_coins for the first elt in array is zero always
    min_num_coins[0] = 0
    #Iterate from 1 to m(not including the m + 1 term) since we know the min_num_of_coins for money = 0
    for i in range(1, m + 1):
         #min_num_of_coins list initialized to floating-point positive infinity
        min_num_coins[i] = inf 
        for coin in coins:
            if i >= coin:
                mnc = min_num_coins[i - coin] + 1
                if mnc < min_num_coins[i]:
                    min_num_coins[i] = mnc
            else:
                break

            
    return min_num_coins[m]

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
