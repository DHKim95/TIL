def solution(n, words):
    answer = [0, 0]
    stack = [words[0]]
    cnt = 1
    
    for i in range(1, len(words)):
        # 번호 맞추기
        cnt %= n
        # 일치 여부 확인
        if words[i] not in stack and words[i][0] == words[i-1][-1]:
            stack.append(words[i])
        else:
            answer = [cnt+1, i // n + 1]
            break
        cnt += 1
    return answer