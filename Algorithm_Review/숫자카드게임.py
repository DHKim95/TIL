N, M = map(int, input().split())

# 최소값중에서 최대값 찾기

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)