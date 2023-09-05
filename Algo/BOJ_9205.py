from collections import deque

def BFS():
    queue = deque()
    queue.append((home_x, home_y))
    while queue:
        x, y = queue.popleft()

        # 20미터 한개씩 50미터면 1000
        if abs(x-rock_x) + abs(y-rock_y) <= 1000:
            print("happy")
            return

        # 편의점 -> 새맥주
        for i in range(N):
            if visited[i] == 0:
                nx, ny = conv_list[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = 1
                    queue.append((nx, ny))
    print('sad')
    return

T = int(input())

for _ in range(T):
    N = int(input())

    home_x, home_y = map(int, input().split())
    conv_list = []
    for _ in range(N):
        x, y = map(int, input().split())
        conv_list.append((x, y))

    rock_x, rock_y = map(int, input().split())

    visited = [0 for _ in range(N+1)]
    BFS()
