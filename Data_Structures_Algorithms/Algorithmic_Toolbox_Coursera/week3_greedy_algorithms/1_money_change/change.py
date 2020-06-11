# Uses python3
import sys

def get_change(m):
    num_coins = 0
    #write your code here
    denoms = [10,5,1]

    rem = m
    while rem!=0:
        for coin in range(len(denoms)):
            num_coins += rem//denoms[coin]
            rem -= (rem//denoms[coin]*denoms[coin])

    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
