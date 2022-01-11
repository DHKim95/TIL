N = int(input())
trophy = []
for _ in range(N):
    trophy.append(int(input()))

cnt, maxnum = 1, trophy[0]

for i in range(0, N - 1):
    if trophy[i + 1] > maxnum:
        cnt += 1
        maxnum = trophy[i + 1]
print(cnt)

cnt, maxnum = 1, trophy[N - 1]
for i in range(N - 1, -1, -1):
    if trophy[i] > maxnum:
        cnt += 1
        maxnum = trophy[i]

print(cnt)