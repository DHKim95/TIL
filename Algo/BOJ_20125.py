N = int(input())

graph = [list(input()) for _ in range(N)]

# 심장 찾기
x, y, head_check = 0, 0, False
for i in range(N):
    for j in range(N):
        if graph[i][j] == '*':
            cen_x, cen_y = i+2, j+1
            head_check = True

    if head_check:
        break

print(cen_x, cen_y)

l_arm, r_arm, back, l_leg, r_leg = 0, 0, 0, 0, 0

# 왼팔
for i in range(cen_y-1):
    if graph[cen_x-1][i] == '*':
        l_arm += 1

# 오른팔
for i in range(cen_y, N):
    if graph[cen_x-1][i] == '*':
        r_arm += 1

# 허리
back_end = 0
for i in range(cen_x, N):
    if graph[i][cen_y-1] == '*':
        back += 1
        back_end = i

# 왼다리
for i in range(cen_x, N):
    if graph[i][cen_y-2] == '*':
        l_leg += 1

# 오다리
for i in range(cen_x, N):
    if graph[i][cen_y] == '*':
        r_leg += 1

print(l_arm, r_arm, back, l_leg, r_leg)