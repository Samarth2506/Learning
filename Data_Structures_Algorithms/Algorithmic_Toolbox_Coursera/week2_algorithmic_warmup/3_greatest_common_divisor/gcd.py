# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a,b):
    
    if a < b:
        b, a = a,b
    
    if b == 0:
        return a
    while True:
        rem = a % b
        if rem == 0:
            return b
        a = gcd_naive(b,rem)
        b = rem

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(gcd_naive(a, b))
