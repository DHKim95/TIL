def DFS(curr):
    visited[curr] = True
    print(chr(curr+65), end=' ')

    for i in range(V):
        if adj_arr[curr][i] and not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)]
visited = [False] * V

for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1  # 여기서 끝내면 방향성있는 표시
    adj_arr[ed][st] = 1

DFS(0)