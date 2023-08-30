N, M, L, K = map(int, input().split())
# N가로, M세로, L트램펄린 한변길이, K 별똥별 수

starlist = []
result = 0

for _ in range(K):
    x, y = map(int, input().split())
    starlist.append((x, y))

for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if starlist[i][0] <= starlist[k][0] and \
                starlist[k][0] <= starlist[i][0]+L and \
                starlist[j][1] <= starlist[k][1] and \
                starlist[k][1] <= starlist[j][1]+L:
                cnt += 1
        result = max(result, cnt)

answer = K - result
print(answer)