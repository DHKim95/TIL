N = int(input())
for i in range(N):

N = int(input())
graph = [[0] * 100 for _ in range(100)]
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    # 길이는 10칸이라서 +10
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            graph[j][i] = 1