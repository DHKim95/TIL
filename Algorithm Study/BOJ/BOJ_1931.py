N = int(input())
# N개의 회의실

max_count = []

# 시작시간과 끝나는 시간을 회의실에 튜플 형태로 배정
for i in range(N):
    a, b = map(int, input().split())
    max_count.append([a, b])

# 끝나는 시간 기준으로 정렬한다.
max_count.sort(key=lambda x: (x[1], x[0]))

end_time = 0
study_count = 0
for i in range(N):
    # 끝나는 시간이 더 적으면 갱신
    if end_time <= max_count[i][0]:
        end_time = max_count[i][1]
        study_count += 1
print(study_count)
