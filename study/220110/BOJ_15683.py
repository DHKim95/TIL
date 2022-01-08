from collections import deque

N, M = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [list(map(int, input().split())) for _ in range(N)]
cctv_lst = []
answer = 0 # 사각지대
visited = [[0] * M for _ in range(N)]
cctv_cnt = 0 # cctv 개수

def solution(count):
    global visited, answer
    # CCTV 개수 전부 체크했다면
    if count == cctv_cnt:
        sub_cnt = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0 and visited[i][j] == 0:
                    sub_cnt += 1
        return sub_cnt

    x, y = cctv_lst[count][0], cctv_lst[count][1]
    for direction in range(4):
        arr = []
        if graph[x][y] == 1:
            arr.append(direction)
        elif graph[x][y] == 2:
            arr.append(direction)
            arr.append((direction + 2) % 4)
        elif graph[x][y] == 3:
            arr.append(direction)
            arr.append((direction - 1) % 4)
        elif graph[x][y] == 4:
            arr.append(direction)
            arr.append((direction - 1) % 4)
            arr.append((direction + 2) % 4)
        elif graph[x][y] == 5:
            arr.append(direction)
            arr.append((direction - 1) % 4)
            arr.append((direction + 1) % 4)
            arr.append((direction + 2) % 4)
        queue = deque()
        for a in arr:
            nx, ny = x + dx[a], y + dy[a]
            


for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            cctv_lst.append((i, j))
            visited[i][j] = 1
            cctv_cnt += 1
        if graph[i][j] == 0:
            answer += 1

solution(0)
print(answer)
