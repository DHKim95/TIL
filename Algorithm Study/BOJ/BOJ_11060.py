N = int(input())

arr = list(map(int, input().split()))
dp = [-1] * N

queue = []
queue.append(0)
dp[0] = 0

while queue:
    now = queue.pop(0)
    jump = arr[now]
    # 최대한 멀리 표시
    for i in range(jump, 0, -1):
        # 범위안에 있고 안가본 경우
        if now + i < N and dp[now + i] == -1:
            # print(dp)
            # 큐에 추가
            dp[now + i] = dp[now] + 1
            queue.append(now + i)


print(dp[-1])