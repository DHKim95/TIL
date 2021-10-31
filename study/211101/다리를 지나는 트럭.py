bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = [0] * bridge_length

    while stack:
        time += 1
        stack.pop(0)
        if truck_weights:


    return stack


print(solution(bridge_length, weight, truck_weights))