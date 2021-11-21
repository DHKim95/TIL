rows, columns = 4, 3
connections = [[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]]
queries = [[2,2,3,1],[1,2,4,2]]

def solution(rows, columns, connections, queries):
    arr = [[0] * columns for _ in range(rows)]
    visited = [[0] * columns for _ in range(rows)]
    answer = []

    for conn in connections:
        x1, y1, x2, y2 = conn
        arr[x1-1][y1-1] = 1
        arr[x2-1][y2-1] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for query in queries:
        cnt = 0
        x1, y1, x2, y2 = query

        for row in range(x1-1, x2):
            for col in range(y1-1, y2):
                pass









    return answer

print(solution(rows, columns, connections, queries))