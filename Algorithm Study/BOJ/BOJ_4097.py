while True:
    N = int(input())

    if N == 0:
        break

    # DP 리스트를 만들기
    dp = [int(input()) for _ in range(N)]

    # 최댓값 계속 갱신
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i] + dp[i-1])

    print(max(dp))