def solution(price, money, count):
    cnt = 0
    for i in range(1, count+1):
        cnt += price * i

    if cnt > money:
        answer = abs(cnt - money)
    else:
        answer = 0
    return answer

print(solution(3, 20, 4))