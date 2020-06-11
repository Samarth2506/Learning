# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    max_capacity = capacity[0]
    
    weights = np.array(weights)
    values = np.array(values)
    per_unit_val = (values/weights).argsort()[::-1]
    
    while max_capacity != 0:
        for i in range(capacity[1]):
            weight_increment = min(max_capacity, weights[per_unit_val[i]])
            max_capacity -= weight_increment
            value +=   (values[per_unit_val[i]]/weights[per_unit_val[i]])*weight_increment
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
