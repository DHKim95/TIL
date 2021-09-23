def dfs(v):
    global cnt
    cnt += 1
    for j in Tree[v]:
        dfs(j)

# 주어진 노드 밑에 몇개인지 파악하기

# 테스트 케이스
T = int(input())

for tc in range(T):
    # 간선의 개수 E와 N
    E, V = map(int, input().split())
    Tree = [[] for _ in range(E+2)] # E의 개수보다 1개 많고 0번째 포함 +2

    arr = list(map(int, input().split()))
    # 그래프 추가
    for i in range(0,E):
        Tree[arr[2*i]].append(arr[2*i+1])

    cnt = 0
    dfs(V)

    print("#{} {}".format(tc+1, cnt))