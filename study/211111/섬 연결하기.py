n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 비용대로 정렬
    visited = [0] * n # 방문표시리스트
    visited[0] = 1


    while sum(visited) != n:
        for cost in costs:
            start, end, c = cost
            if visited[start] or visited[end]:
                if visited[start] and visited[end]:
                    continue
                else:
                    visited[start] = 1
                    visited[end] = 1
                    answer += c
                    break

    return answer

print(solution(n, costs))