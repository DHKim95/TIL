N = int(input())

# 갯수 더하기
cnt = 0
for i in range(1, N+1):
    # 합 더하기
    sub_cnt = 0
    for j in range(i, N+1):
        sub_cnt += j
        # 숫자 체크
        if sub_cnt == N:
            cnt += 1
            break
        elif sub_cnt > N:
            break
print(cnt)