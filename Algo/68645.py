def solution(n):
    answer = []
    graph = [[0 for _ in range(i+1)] for i in range(n)]
    x, y = -1, 0
    number = 1

    for i in range(n):
        for j in range(i, n):
            # print(i, j, number)
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            graph[x][y] = number
            number += 1

    for i in graph:
        answer.extend(i)

    return answer

solution(4)