# python3
import sys

# my solution
# def compute_min_refills(distance, tank, stops):
#     # write your code here
#     refills = 0
#     curr_dist = 0
    
#     for i in range(len(stops)-1):
#             curr_dist = stops[i]
#             fuel_rem = tank - curr_dist
#             dist_next_stop = stops[i+1] - stops[i]
#             if dist_next_stop <= fuel_rem:
#                 continue

#             if fuel_rem < dist_next_stop:
#                 refills +=1 
#             if tank < dist_next_stop:
#                 return -1
            
#     return refills

def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_refill = 0
    while current_refill <= distance:
        last_refill = current_refill
        while current_refill <= distance and stops[current_refill+1] - stops[last_refill] <= tank:
            current_refill += 1
        if current_refill == last_refill:
            return "IMPOSSIBLE"
        if current_refill <= distance:
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    d, m, *stops = map(int, sys.stdin.readline().split())
    print(compute_min_refills(d, m, stops))
