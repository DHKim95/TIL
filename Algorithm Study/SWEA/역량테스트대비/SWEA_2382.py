T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(T):
    answer = 0
    N, M, K = map(int, input().split())
    virus = {}

    for i in range(K):
        x, y, n, direction = map(int, input().split())
        virus[(x,y)] = [n,d,n]


    print("#{} {}".format(tc+1, answer))