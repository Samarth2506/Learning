# Uses python3
def calc_fib(n):

    # Naive implementation : n = 40 takes 32.38 s
    # if (n <= 1):
    #     return n

    # return calc_fib(n - 1) + calc_fib(n - 2)

    # n = 40 takes 0.005 s!
    arr = list(range(n+2))
    
    arr[0] = 0
    arr[1] = 1
    
    for i in range(2,len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]

n = int(input(n))

print(calc_fib(n))
