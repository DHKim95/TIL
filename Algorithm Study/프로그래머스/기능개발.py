def solution(progresses, speeds):
    answer = []
    now_time = 0
    cnt = 0

    while len(progresses) > 0:
        if progresses[0] + (now_time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            now_time += 1
    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))