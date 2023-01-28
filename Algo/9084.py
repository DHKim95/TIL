T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for i in arr:
        for num in range(1, M+1):
            if num - i >= 0:
                dp[num] += dp[num - i]

    print(dp[M])
