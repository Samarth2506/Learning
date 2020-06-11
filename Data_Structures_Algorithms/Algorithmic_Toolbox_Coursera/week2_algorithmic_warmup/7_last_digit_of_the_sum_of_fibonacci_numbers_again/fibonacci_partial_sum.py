# Uses python3
import sys
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def fib_sum(n):
    if n <= 1:
        return n
    
    sum_fib = get_fibonacci(n+2) - 1
    
    return sum_fib
    
    
def fib_partial_sum(m,n):
    first_sum = fib_sum(m-1)
    second_sum = fib_sum(n)
    
    return (second_sum - first_sum)

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))