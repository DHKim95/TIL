N = int(input())

telephone = []
for _ in range(N):
    telephone.append(list(map(int, input().split())))

telephone.sort()

# print(telephone)

dp = [1] * N
for i in range(N):
    for j in range(i):
        # 안겹쳐지는거 체크해서 더해주기
        if telephone[i][1] > telephone[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 전체에서 최대를 빼서 필요한 전기 개수
print(N - max(dp))