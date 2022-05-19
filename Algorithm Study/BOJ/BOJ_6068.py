N = int(input())

time_lst = []
for _ in range(N):
    time_lst.append(list(map(int, input().split())))

# 필요한시간, 끝내야하는시간
time_lst.sort(key=lambda x: x[1])
time_cnt = 0
max_time = 1e9
check = False

for time, finish_time in time_lst:
    time_cnt += time
    if time_cnt > finish_time:
        print(-1)
        check = True
        break
    max_time = min(max_time, finish_time - time_cnt)

if check:
    pass
else:
    print(max_time)