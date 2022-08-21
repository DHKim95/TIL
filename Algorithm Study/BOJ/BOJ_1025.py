import math

N, M = map(int, input().split())

graph = [input() for _ in range(N)]
answer = -1

for i in range(N):
    for j in range(M):
        for a in range(-N, N):
            for b in range(-M, M):
                number = ''
                x, y = i, j
                while 0 <= x < N and 0 <= y < M:
                    number += graph[x][y]
                    if a == 0 and b == 0:
                        break

                    if int(math.sqrt(int(number))) ** 2 == int(number):
                        answer = max(int(number), answer)

                    x += a
                    y += b

print(answer)

