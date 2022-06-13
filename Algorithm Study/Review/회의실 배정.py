N = int(input())

class_lst = []
for _ in range(N):
    start, end = map(int, input().split())
    class_lst.append((start, end))

class_lst.sort(key=lambda x: (x[1], x[0]))
# class_lst = sorted(class_lst, key=lambda x: (x[1], x[0]))

cnt = 0
last_time = 0
for start, end in class_lst:
    if start >= last_time:
        cnt += 1
        last_time = end

print(cnt)