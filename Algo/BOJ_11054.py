N = int(input())

arr = list(map(int, input().split()))
up_list = [1 for _ in range(N)]
down_list = [1 for _ in range(N)]
answer = [0 for _ in range(N)]

# 올라가는거 구하기
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and up_list[i] < up_list[j] + 1:
            up_list[i] = up_list[j]+1

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[i] > arr[j] and down_list[i] < down_list[j] + 1:
            down_list[i] = down_list[j] + 1

    answer[i] = up_list[i] + down_list[i] - 1

print(max(answer))