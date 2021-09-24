N, M = map(int, input().split())

# 빈 리스트를 만들고 1차 리스트를 append 한다.
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 2
# 행의 공간을 확보해두고 자리를 바꾼다.
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

# 3
# 리스트 내포 방식
arr = [list(map(int, input().split())) for _ in range(N)]
