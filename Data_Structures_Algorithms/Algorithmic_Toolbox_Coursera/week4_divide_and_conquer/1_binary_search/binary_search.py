# Uses python3
import sys
import math
def binary_recurse(a,low, high, key):
    if high < low:
        return -1
    mid = low + (high - low)//2
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_recurse(a, low, mid-1,key)
    else:
        return binary_recurse(a,mid+1,high,key)

def binary_search(a, x):
    answer = []
    low, high = 0, len(a)-1
    for xi in x:
        answer.append(binary_recurse(a,low,high,xi))
    return answer
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end = ' ')
