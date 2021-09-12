N, C = map(int, input().split()) # N은 개수, C는 최대 수

arr = list(map(int, input().split()))
dic = {}

# 딕셔너리에 카운팅 해준다.
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 빈도수별로 정렬을 해준다.
new_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for a, b in new_dic:
    for j in range(b):
        print(a,end=' ')