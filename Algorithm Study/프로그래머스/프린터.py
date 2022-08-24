from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(val, idx) for idx, val in enumerate(priorities)])

    while queue:
        x = queue.popleft()
        # 다시 넣어주기
        if queue and max(queue)[0] > x[0]:
            queue.append(x)
        else:
            answer += 1
            if x[1] == location:
                break

    return answer