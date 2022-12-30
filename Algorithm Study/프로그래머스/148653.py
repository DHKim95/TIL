def solution(storey):
    answer = 0

    while storey:
        # 나머지 확인
        x = storey % 10

        # 5보다 클 경우는 횟수만큼 더하고 5일경우는 상황보기
        if x > 5 or (x == 5 and (storey // 10) % 10 >= 5):
            storey += (10 - x)
            answer += (10 - x)
        # 5보다 작으면 더하기만 한다.
        else:
            answer += x

        storey //= 10
    return answer