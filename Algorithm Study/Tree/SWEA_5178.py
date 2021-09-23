# 좌우로 해당 값까지 밑에 구간들 더해주기
def dfs(v):
    if 2 * v <= N:
        if Tree[2*v] == 0:
            dfs(2*v)
        Tree[v] += Tree[2*v]

    if 2 * v + 1 <= N:
        if Tree[2*v+1] == 0:
            dfs(2*v+1)
        Tree[v] += Tree[2*v+1]

T = int(input())

for tc in range(T):
    # N은 노드개수, M은 리프 개수, L은 출력할 값
    N, M, L = map(int, input().split())
    Tree = [0 for _ in range(N+1)]
    # 트리에 유효한 값 넣어주기
    for i in range(M):
        a, b = map(int, input().split())
        Tree[a] = b

    dfs(L)

    print("#{} {}".format(tc+1, Tree[L]))