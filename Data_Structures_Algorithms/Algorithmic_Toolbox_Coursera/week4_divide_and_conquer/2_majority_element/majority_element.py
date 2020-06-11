# Uses python3
import sys

def get_majority_element(a):
    counter = {}
    for ai in a:
        if ai in counter.keys():
            counter[ai] += 1
            if counter[ai] > len(a)/2:
                return 1
        else:
            counter[ai] = 1
    count = max(counter.values())
    return 0
     

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
