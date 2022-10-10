def solution(cacheSize, cities):
    answer = 0
    lst = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        # 있으면 제거하고 다시넣어준다.
        if city in lst:
            answer += 1
            lst.remove(city)
            lst.append(city)
        # 캐시 없다면
        else:
            answer += 5
            if len(lst) >= cacheSize:
                lst.pop(0)
            lst.append(city)
    
    return answer