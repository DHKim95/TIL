N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

for i in range(len(lst)-1):
    min_value = i
    for j in range(i+1, len(lst)):
        if lst[min_value] > lst[j]:
            min_value = j
    lst[j], lst[min_value] = lst[min_value], lst[j]