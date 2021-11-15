routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0])) # 정렬시키기

    # print(routes)
    end = -30001 # 끝지점
    for route in routes:
        # 범위안에 안들었으면 카메라가 필요한거
        if end < route[0]:
            answer += 1
            end = route[1]

    return answer

print(solution(routes))