T = int(input())

for tc in range(T):
    N = int(input())
    graph = list(map(int, input().split()))

    print("#{} {}".format(tc+1, max(graph)-min(graph)))