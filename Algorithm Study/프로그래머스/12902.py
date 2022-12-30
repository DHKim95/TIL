def solution(n):
    answer = 0

    dp = [3, 11]
    # dp = [0] * n
    # dp[0] = 3
    # dp[1] = 11

    if n <= 4:
        return dp[n // 2 - 1]
    else:
        for i in range(2, n // 2):
            dp.append((dp[i - 1] * 4 - dp[i - 2]) % 1000000007)

    answer = dp[-1]
    return answer