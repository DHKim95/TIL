N = int(input())

people = 0
house = []
for _ in range(N):
    diff, cnt = map(int, input().split())
    house.append((diff, cnt))
    people += cnt

house.sort()

people_count = 0
for diff, cnt in house:
    people_count += cnt
    if people_count > (people / 2):
        print(diff)
        break