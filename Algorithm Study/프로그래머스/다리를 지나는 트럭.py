def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0 for _ in range(bridge_length)]

    while stack:
        answer += 1
        stack.pop(0)

        if truck_weights:
            # 빈공간이 있으면 넣는다.
            if sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
            # 빈공간이 없더라도 갯수 유지
            else:
                stack.append(0)

    return answer