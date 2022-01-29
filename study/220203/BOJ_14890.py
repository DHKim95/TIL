def runway(road):
    for j in range(1, N):
        # 차이가 1 이상
        if abs(road[j] - road[j-1]) > 1:
            return False

        # 오른쪽 스캔
        if road[j] < road[j - 1]:
            for idx in range(L):
                # 범위가 넘어가거나 이미 설치되었거나 낮은곳의 높이가 다른경우
                if j + idx >= N or visited[j+idx] == 1 or road[j] != road[j + idx]:
                    return False

                # 높이가 같은 경우
                if road[j] == road[j+idx]:
                    visited[j+idx] = True

        # 왼쪽으로 스캔
        elif road[j] > road[j-1]:
            for idx in range(L):
                if j - idx - 1 < 0 or road[j - 1] != road[j - idx - 1] or visited[j - idx - 1]:
                    return False

                if road[j - 1] == road[j - idx - 1]:
                    visited[j- idx - 1] = True

    # 문제 없이 설치
    return True


N, L = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    visited = [0 for _ in range(N)]
    if runway((graph[i])):
        cnt += 1

for i in range(N):
    visited = [0 for _ in range(N)]
    if runway([graph[j][i] for j in range(N)]):
        cnt += 1

print(cnt)
