def solution(progresses, speeds):
    answer = []
    while progresses:
        prog = progresses.pop(0)
        speed = speeds.pop(0)

        answer.append((100 - prog) // speed)


    return answer



print(solution([93, 30, 55], [1, 30, 5]))