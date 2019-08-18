#Uses Python3
import math
import sys
def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        r = a%b
        return euclid_gcd(b, r)   


def lcm_fast(a, b):
    
    return  (a * b) // euclid_gcd(a, b) # // represent floor division, that is the


     
if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_fast(a, b))  

