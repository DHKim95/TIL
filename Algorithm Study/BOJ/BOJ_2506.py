N = int(input())

arr = list(map(int, input().split()))

answer = 0 # 전체 합
cnt = 0 # 서브함수
check = False # 체크
for num in arr:
    # 0일 경우 체크 함수와 서브숫자를 0으로 만들어준다.
    if num == 0:
        check = False
        cnt = 0

    # 0이 아닐경우
    elif num != 0:
        # 체크일경우 더 더해주기
        if check == True:
            cnt += 1
            answer += cnt
        # 체크가 아닐경우 체크로 바꿔주기
        else:
            cnt += 1
            answer += cnt
            check = True

print(answer)