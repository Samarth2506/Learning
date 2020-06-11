# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    results_union = []
    #write your code here
    segments.sort(key = lambda x: x[1])
    max_right = segments[0][1]
    points.append(max_right)co
    for i in range(len(segments)):
        if max_right < segments[i][0]:
            max_right = segments[i][1]
            points.append(max_right)
        
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
