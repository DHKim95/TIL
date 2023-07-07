N, B = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

def mul(N, graph_a, graph_b):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += graph_a[i][k] * graph_b[k][j]
            result[i][j] %= 1000
    return result

def cal(N, B, graph):
    if B == 1:
        return graph
    elif B == 2:
        return mul(N, graph, graph)
    else:
        sub = cal(N, B // 2, graph)
        # 제곱끼리를 한번 곱해줘야함
        if B % 2 == 0:
            return mul(N, sub, sub)
        # 홀수면 1개가 남기 때문에 곱해주기
        else:
            sub2 = mul(N, sub, sub)
            return mul(N, sub2, graph)

answer = cal(N, B, graph)

for i in answer:
    for j in i:
        print(j % 1000, end=' ')
    print()