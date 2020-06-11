# Uses python3
import sys

def get_fibonacci_huge_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current 

def get_period(m):
    previous = 0
    current = 1
    
    for i in range(m*m + 1):
        previous, current = current, (previous+current)%m
        if previous == 0 and current == 1:
            return i + 1
        
def get_fib_huge(n,m):

    len_rep = get_period(m)

    rem = n%len_rep

    return get_fibonacci_huge_naive(rem)%m
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
