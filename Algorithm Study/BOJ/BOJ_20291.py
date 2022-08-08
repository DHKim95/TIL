N = int(input())

dic = {}
for _ in range(N):
    words = input().split('.')[1]

    if words not in dic:
        dic[words] = 1
    else:
        dic[words] += 1

ans = list(dic.keys())
ans.sort()

for i in ans:
    print(i, dic[i])
