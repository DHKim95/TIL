N = int(input())

work_arr = []
cost_arr = []
dp = [0] * (N+1)

for _ in range(N):
    work, cost = map(int, input().split())

    work_arr.append(work)
    cost_arr.append(cost)

max_value = 0
for i in range(N):
    print(dp)
    # 날짜안에 들어오는지 확인
    if work_arr[i] + i <= N:
        # 끝나는 날 비용이 얼만지 계산해서 최대값을 넣는다.
        dp[i + work_arr[i]] = max(dp[i + work_arr[i]], dp[i]+cost_arr[i])

    # 값 채워넣기(최대값으로)
    dp[i+1] = max(dp[i], dp[i+1])

print(max(dp))