N, K  = map(int, input().split()) # 학생 수, 최대인원 수
lst = [0] * 12

for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        lst[b*2-2] += 1
    elif a == 1:
        lst[b*2-1] += 1

cnt = 0
idx = 0
check = False

while True:
    if sum(lst) == 0 or idx == 12:
        break

    if lst[idx] >= K:
        lst[idx] -= K
        check = True
    elif 0 < lst[idx] < K:
        lst[idx] = 0
        check = True

    if check == True and lst[idx] == 0:
        idx += 1
        cnt += 1
        check = False
    elif check == False:
        idx += 1
    elif check == True:
        cnt += 1
    # print(lst)
    # print(cnt)

print(cnt)

