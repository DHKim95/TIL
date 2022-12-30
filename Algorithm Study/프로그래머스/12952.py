def solution(n):
    answer = 0
    visited = [0] * n

    def check(graph, row):
        for i in range(row):
            # 겹치기
            if graph[row] == graph[i] or abs(row - i) == abs(graph[row] - graph[i]):
                return False
        return True

    def queen(graph, n, row):
        cnt = 0

        if row == n:
            return 1

        for i in range(n):
            graph[row] = i

            if check(graph, row):
                cnt += queen(graph, n, row + 1)

        return cnt

    answer = queen(visited, n, 0)

    return answer