from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 위쪽 왼쪽 먼저
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

baby_size = 2 # 아기상어크기
a = 0 # 크기
shark_eat = 0 # 먹는시간

def BFS(x, y, baby_size):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위 안
            if 0 <= nx < N and 0 <= ny < N:
                # 자신과 같으면 지나가기
                if (graph[nx][ny] == baby_size or graph[nx][ny] == 0) and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                # 먹을수 있는 물고기
                elif graph[nx][ny] < baby_size and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                    result.append([distance[nx][ny], nx, ny])

while True:
    result = []
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    # print(graph)
    for i in range(N):
        for j in range(N):
            # 아기상어 발견
            if graph[i][j] == 9:
                BFS(i, j, baby_size)
                graph[i][j] = 0

    # 먹은 물고기가 있으면 정렬
    if len(result) != 0:
        result.sort()
        min_dis, now_x, now_y = result.pop(0)
        shark_eat += min_dis # 시간더하기
        a += 1# 같은 수 크기
        graph[now_x][now_y] = 9
    else:
        break
    print(a)
    if a == baby_size:
        # print("언제지", a)
        baby_size += 1
        a = 0

print(shark_eat)

'''
아기상어는 자기보다 크기가 작은 물고기를 먹을 수 있고 크기가 같다면 지나갈 수만 있고 크기가 자신보다 크다면 지나갈 수 없다.
bfs를 돌면서 자신보다 크기가 작은 물고기(먹을수 있는 물고기)를 만나면 result 리스트에 거리, x좌표, y좌표 순으로 넣어준다.
result 리스트를 sort 정렬 시켜서 가장 거리가 짧은 물고기를 먹고 (거리가 같다면 x좌표, y좌표 순으로 오름차순 정렬된다.) exp를 +1 해주고 만약 exp와 size가 같다면 size를 1 증가시켜 준다.
아기상어가 먹을수 있는 물고기가 없을때 까지 계속 돌아주고 아기상어가 물고기를 잡아먹은 시간은 이동거리와 똑같으므로 distance배열로 구해줬다.'''