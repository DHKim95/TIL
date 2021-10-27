from collections import deque

def bfs(N):
    queue = deque()
    queue.append(N)
    cnt = 0
    check = False

    while queue:
        # 안에 횟수 반복
        for _ in range(len(queue)):
            v = queue.popleft()
            # 방문하지 않았으면 방문 처리
            if graph[v] == 0:
                graph[v] = 1
                # 도착지점에 도달하면 끝내기
                if v == K:
                    check = True
                    break

                # 갈 수 있는 3가지 방향으로 탐색
                if v - 1 >= 0:
                    queue.append(v - 1)
                if v + 1 <= 100000:
                    queue.append(v + 1)
                if v * 2 <= 100000:
                    queue.append(v * 2)

        # 도달했다면 최소 횟수 출력
        if check:
            print(cnt)
            break
        cnt += 1 # 횟수 추가

N, K = map(int, input().split())
graph = [0] * 100001 # 갈 수 있는 최대 공간
bfs(N)