N = int(input())

lst = []
for _ in range(N):
    lst.append(float(input()))

# 높은거 찾기
for i in range(1, N):
    lst[i] = max(lst[i], lst[i] * lst[i-1])

print("{:.3f}".format(max(lst)))