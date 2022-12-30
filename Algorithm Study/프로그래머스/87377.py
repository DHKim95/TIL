import numbers

def solution(line):
    
    dot_list = []
    for i in range(len(line)):
        a, b, c = line[i]
        for j in range(i+1, len(line)):
            d, e, f = line[j]
            
            divide = a*e - b*d
            # 직선이 평행하거나 일치
            if divide == 0:
                continue
            
            # 교점구하기
            x = (b*f - c*e) / divide
            y = (c*d - a*f) / divide
            if x.is_integer() and y.is_integer() :
            # if (int(x) == x) and (int(y) == y):
                dot_list.append((int(x), int(y)))
    
    # 중복제거
    dot_list = list(set(dot_list))
    # print(dot_list)
    dot_list.sort(key=lambda x: (x[1] - x[0]), reverse=True)
    # print(dot_list)
    
    x_list, y_list = [], []
    for dot in dot_list:
        x_list.append(dot[0])
        y_list.append(dot[1])
    x_min, x_max = min(x_list), max(x_list)
    y_min, y_max = min(y_list), max(y_list)
    
    graph = [['.' for _ in range(x_min, x_max+1)] for _ in range(y_min, y_max+1)]
    
    # 좌표 맞추기
    for dot in dot_list:
        x = y_max - dot[1]
        y = dot[0] - x_min
        graph[x][y] = '*'
        
    answer = []
    for g in graph:
        answer.append(''.join(g))
    return answer