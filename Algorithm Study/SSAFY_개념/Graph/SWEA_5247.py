from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    queue = deque()
    visited = [0] * 1000001
    queue.append(N)

    while queue:
        v = queue.popleft()
        # 원하던 숫자 찾았을 경우 출력
        if v == M:
            print("#{} {}".format(tc+1, visited[v]))
            break

        # 4개 갈수 있는 곳 다 하기
        for nv in [v+1, v-1, v*2, v-10]:
            # 범위안에 숫자가 있고 방문하지 않았으면 횟수 추가해주기
            if 0 <= nv <= 1000000 and visited[nv] == 0:
                queue.append(nv)
                visited[nv] = visited[v] + 1