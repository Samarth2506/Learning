#Uses python3

import sys

def is_greater(digit, max_digit):
    return digit + max_digit > max_digit + digit

def largest_number(a):
    #write your code here
    answer = ""
    
    while len(a) > 0:
        max_digit = '0'
        for digit in a:
            if is_greater(digit,max_digit):
                max_digit = digit
        answer += max_digit
        a.remove(max_digit)
    return "".join([str(i) for i in answer])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
