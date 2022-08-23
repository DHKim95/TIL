from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    cnt = 0

    while True:
        if q1_sum == q2_sum:
            return cnt

        if cnt == len(q1) * 2:
            return -1

        if q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else:
            num = q2.popleft()
            q1.append(num)
            q1_sum += num
            q2_sum -= num

        cnt += 1