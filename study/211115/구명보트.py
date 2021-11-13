people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    cnt_people = len(people) # 총 운반 횟수
    sort_people = sorted(people, reverse=True)
    start = 0
    end = cnt_people - 1 # 인덱스라 -1

    # 두개가 바뀌면 전부 운반
    while start < end:
        # 두개가 들어갈 경우 운반횟수를 하나씩 감소시킨다.
        if sort_people[start] + sort_people[end] <= limit:
            end -= 1
            cnt_people -= 1
        start += 1 # 이거는 운반횟수 감소 x
    return cnt_people


print(solution(people, limit))