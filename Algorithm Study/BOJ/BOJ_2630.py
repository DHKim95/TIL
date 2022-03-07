N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
answer = []

def solve(x, y, N):
    number = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if number != graph[i][j]:
                # 1사분면
                solve(x, y, N//2)
                # 2사분면
                solve(x, y+N//2, N//2)
                # 3사분면
                solve(x+N//2, y, N//2)
                # 4사분면
                solve(x+N//2, y+N//2, N//2)
                return
    if number == 0:
        answer.append(0)
    else:
        answer.append(1)

solve(0, 0, N)

print(answer.count(0))
print(answer.count(1))