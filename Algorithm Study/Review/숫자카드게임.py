N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

    # min_value = 10001
    # for a in data:
    #     min_value = min(min_value, a)
    # result = max(result, min_value)

print(result)