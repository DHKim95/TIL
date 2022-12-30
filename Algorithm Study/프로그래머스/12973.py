def solution(s):
    dq = []
    for i in range(len(s)):
        # 덱에 원소가 있고 현재 뽑아내는 원소가 마지막에 있는 원소랑 같으면 마지막 제거
        if dq and dq[-1] == s[i]:
            dq.pop()
        # 아니면 추가
        else:
            dq.append(s[i])

    # 원소가 남아있으면 0반환
    if dq:
        return 0
    else:
        return 1