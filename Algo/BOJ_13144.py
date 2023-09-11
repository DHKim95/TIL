N = int(input())

arr = list(map(int, input().split()))

start, end = 0, 0
dp = [0] * 100001
# dp = [0] * 6
answer = 0

while start < N and end < N:
    # 중복숫자 확인
    if dp[arr[end]] == 0:
        dp[arr[end]] = 1
        end += 1
        answer += (end - start) # 개수 추가
    else:
        dp[arr[start]] = 0
        start += 1
    # print(dp)

print(answer)