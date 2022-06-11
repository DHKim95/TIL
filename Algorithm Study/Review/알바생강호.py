N = int(input())

cnt = 0
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(N):
    # 순위별로 계산
    num = arr[i] - i
    # 양수면 추가하기
    if num > 0:
        cnt += num

print(cnt)