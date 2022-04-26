T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    # i원 동전을 이용해 j원을 만드는 경우의 수
    # 동전의 종류로 할당
    for i in range(N):
        for j in range(coins[i], M+1):
            # print(i, j)
            dp[j] += dp[j-coins[i]]

    print(dp[M])