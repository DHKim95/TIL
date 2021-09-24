T = int(input())

for tc in range(T):
    money = list(map(int, input().split()))
    month = list(map(int, input().split()))
    dp = [0] * 12

    dp[0] = min(money[0] * month[0], money[1]) # 1개월권과 1일권 비교
    dp[1] = dp[0] + min(money[0] * month[1], money[1]) # 1개월권과 1일권 비교
    dp[2] = min(dp[1] + min(money[0] * month[2], money[1]), money[2]) # 3개월권과 각각 계산한 금액

    for i in range(3, 12):
        # 지지난달과 3개월권 vs 전달까지 요금과 이번달 1일권과 1개월권
        dp[i] = min(dp[i-3] + money[2], dp[i-1] + min(money[0] * month[i], money[1]))

    # 전체 금액과 1년권 비교
    dp[11] = min(dp[11], money[3])

    print("#{} {}".format(tc+1, dp[11]))