N, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
state = [[[] for _ in range(N)] for _ in range(N)]
chess = []

for i in range(K):
    x, y, direction = map(int, input().split())
    state[x-1][y-1].append(i)
    chess.append([x-1, y-1, direction-1])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 1


check = False
while cnt <= 1000:
    for i in range(K):
        if move(i) == False:
            check = True
            break

    cnt += 1
    if check == True:
        break

if cnt <= 1000:
    print(cnt)
else:
    print(-1)

