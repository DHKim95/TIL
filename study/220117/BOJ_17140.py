R, C, K = map(int, input().split())

graph = []

for _ in range(3):
    sub_lst = list(map(int, input().split()))
    graph.append(sub_lst)


time = 0
check = False
while time <= 100:
    if R <= len(graph) and C <= len(graph[0]) and graph[R-1][C-1] == K:
        print(time)
        check = True
        break

    time += 1
    max_column = 0
    next_lst = []

    # R연산하기
    if len(graph) >= len(graph[0]):
        for rows in graph:
            row_lst = []
            row_dic = {}
            # 체크해주기
            for row in rows:
                if row in row_dic:
                    row_dic[row] += 1
                else:
                    row_dic[row] = 1

            sort_row = sorted(row_dic.items(), key=lambda x: (x[1], x[0]))
            sort_row = list(sort_row)
            for number, cnt in sort_row:
                if number == 0:
                    continue
                row_lst.append(int(number))
                row_lst.append(cnt)
            max_column = max(max_column, len(row_lst))
            next_lst.append(row_lst)

        # 0채워넣기
        for rows in next_lst:
            if len(rows) < max_column:
                for _ in range(max_column - len(rows)):
                    rows.append(0)
        graph = next_lst
    # C연산
    elif len(graph) < len(graph[0]):
        graph = list(map(list, zip(*graph)))
        for rows in graph:
            row_lst = []
            row_dic = {}
            # 체크해주기
            for row in rows:
                if row in row_dic:
                    row_dic[row] += 1
                else:
                    row_dic[row] = 1

            sort_row = sorted(row_dic.items(), key=lambda x: (x[1], x[0]))
            sort_row = list(sort_row)
            for number, cnt in sort_row:
                if number == 0:
                    continue
                row_lst.append(int(number))
                row_lst.append(cnt)
            max_column = max(max_column, len(row_lst))
            next_lst.append(row_lst)

        # 0채워넣기
        for rows in next_lst:
            if len(rows) < max_column:
                for _ in range(max_column - len(rows)):
                    rows.append(0)

        grpah = list(map(list, zip(*next_lst)))
        continue

if not check:
    print(-1)