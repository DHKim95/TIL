from collections import deque

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

animal = deque()
water = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        # 물 표시
        if graph[i][j] == '*':
            water.append((i, j))
            visited[i][j] = 1
        # 출발점
        elif graph[i][j] == 'S':
            animal.append((i, j))
            visited[i][j] = 1
        # 벽 못가게 막기
        elif graph[i][j] == 'X':
            visited[i][j] = 1

check= False

def main():
    global check
    cnt = 0
    while animal:
        for i in range(len(water)):
            x, y = water.popleft()
            for j in range(4):
                wx = x + dx[j]
                wy = y + dy[j]
                if 0 <= wx < R and 0 <= wy < C and graph[wx][wy] == '.':
                    water.append((wx, wy))
                    graph[wx][wy] = '*'
                    visited[wx][wy] = 1

        cnt += 1

        # 평소와 다르게 있는거 한번에 진행 -> 물차는것 떄문에에
        for _ in range(len(animal)):
            x, y = animal.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        animal.append((nx, ny))
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 'D':
                        check = True
                        print(cnt)
                        return

main()
if check == False:
    print("KAKTUS")