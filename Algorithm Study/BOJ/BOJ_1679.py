from collections import deque

def bfs(N):
    queue = deque()
    queue.append(N) # N점을 큐에 넣기
    cnt = 0 # 횟수 체크
    check = False # 체크변수

    while queue:
        print(queue)
        for _ in range(len(queue)):
            v = queue.popleft()
            if not graph[v]:
                graph[v] = True
                # 해당 위치 찾으면 탈출
                if v == K:
                    check = True
                    break

                # 3가지 경우의 수 다 해보기
                if v - 1 >= 0:
                    queue.append(v - 1)
                if v + 1 <= 100000:
                    queue.append(v + 1)
                if v * 2 <= 100000:
                    queue.append(v * 2)

        if check:
            print(cnt)
            break
        cnt += 1

N, K = map(int, input().split())
graph = [0] * 100001
bfs(N)