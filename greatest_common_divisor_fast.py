#Uses Python3

def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        r = a%b
        return euclid_gcd(b, r)     



if __name__ == "__main__":
    a, b = map(int, input().split()) 
    print(euclid_gcd(a, b))