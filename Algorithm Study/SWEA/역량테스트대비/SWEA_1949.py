T = int(input()) # 테스트 케이스
for tc in range(T):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    print(graph)