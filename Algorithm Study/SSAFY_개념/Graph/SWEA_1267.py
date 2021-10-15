from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split()) # V는 정점, E는 간선
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    cnt_lst = [0 for _ in range(V+1)]
    arr = list(map(int, input().split()))

    # 그래프 만들어주기
    for i in range(E):
        graph[arr[i*2]].append(arr[i*2+1])
        cnt_lst[arr[i*2+1]] += 1 # 자기한테 들어오는 경로 표시

    # cnt_lst에 0인부분은 부모가 없다는 뜻이므로 큐에 먼저 넣어준다.
    queue = deque()
    for i in range(1, V+1):
        if cnt_lst[i] == 0:
            queue.append(i)
            visited[i] = 1

    print("#{} ".format(tc),end='')
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            cnt_lst[i] -= 1
            # 방문하지 않았고 카운트리스트가 0일 경우 -> 자기한테 들어오는 경로가없는 경우
            if visited[i] == 0 and cnt_lst[i] == 0:
                queue.append(i)
                visited[i] = 1
    print()
