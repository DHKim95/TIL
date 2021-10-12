def DFS(idx, graph):
    global cnt
    if idx == N: # 벽돌을 다쓴다면
        block_cnt = 0
        # 0의 개수 카운트해서 전체에서 빼주면 남은 벽돌 개수
        # 1만 남는줄 알았는데 다른 숫자도 남는다..
        for i in range(H):
            block_cnt += graph[i].count(0)
        result = W * H - block_cnt
        # 최솟값 갱신
        if result < cnt:
            cnt = result
        return




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
    # N개의 벽돌, W는 가로, H는 세로
    N, W, H = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(H)]

    cnt = 999999999

    DFS(0, graph)