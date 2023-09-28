N = int(input())

works = []
visited = [0] * 1001
answer = 0

for _ in range(N):
    d, w = map(int, input().split())
    works.append((d, w))

# 일 양이 많은것 우선으로 배정
works.sort(key=lambda x: (x[1], -x[0]), reverse=True) # 뒷정렬은 상관없는듯

for day, work in works:
    while day > 0 and visited[day]:
        day -= 1

    if day != 0:
        visited[day] = 1
        answer += work

print(answer)
    
