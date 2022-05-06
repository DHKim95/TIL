T = int(input())

for _ in range(T):
    # 동전 가지 수
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input()) # 만드는 금액

    # 경우의 수
    dp = [0] * (M+1)
    dp[0] = 1

    for c in coins:
        # print(c)
        # 내가 만드는 금액이 i보다 크지 않을 때
        for i in range(M+1):
            if i - c >= 0:
                dp[i] += dp[i - c]

    print(dp[-1])
