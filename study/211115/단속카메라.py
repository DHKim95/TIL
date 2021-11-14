routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    print(routes)
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))

    end = -30001
    for cam in routes:
        start = cam[0]
        print(start, end)
        if start <= end:
            continue
        answer += 1
        end = cam[1]

    return answer

print(solution(routes))