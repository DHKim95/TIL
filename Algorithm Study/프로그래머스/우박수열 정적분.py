def solution(k, ranges):
    answer = []
    arr = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = (k * 3 + 1)
        arr.append(k)
    
    # 사이마다 영역 구하기
    area_lst = []
    for i in range(len(arr)-1):
        x1 = arr[i]
        x2 = arr[i+1]
        
        area = (x1 + x2) / 2
        area_lst.append(area)
    # print(area_lst)
    
    # 정해진 범위만큼 더하기
    for r in ranges:
        a = r[0]
        b = len(area_lst) + r[1]
        
        if a > b:
            answer.append(-1)
        else:
            answer.append(sum(area_lst[a:b]))
    
    return answer