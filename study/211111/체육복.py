n = 5
lost = [2,4]
reserve = [1,3,5]

# n = 5
# lost = [2,4]
# reserve = [3]

def solution(n, lost, reserve):
    # 학생수 표시
    answer = [1] * n

    # 여벌 남는사람과 없는사람 체크해주기
    for i in reserve:
        answer[i-1] += 1
    for i in lost:
        answer[i-1] -= 1

    # 한바퀴돌기
    for i in range(n):
        # 옷이 없다면
        if answer[i] == 0:
            # 인덱스 체크해주기
            if i > 0 and answer[i-1] == 2:
                answer[i] = 1
                answer[i-1] = 1
            elif i+1 < n and answer[i+1] == 2:
                answer[i] = 1
                answer[i+1] = 1

    return n - answer.count(0)

print(solution(n, lost, reserve))