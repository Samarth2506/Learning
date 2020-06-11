# python3

import sys

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    # a,b = int(sys.argv[1]), int(sys.argv[2])
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
