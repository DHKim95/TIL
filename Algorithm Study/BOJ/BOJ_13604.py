J, R = map(int, input().split())
arr = list(map(int, input().split()))

lst = [[] for _ in range(J+1)]

for i in range(R):
    for j in range(J):
        lst[j+1].append(arr[i*J+j])

max_index = 0
max_value = 0
for i in range(len(lst)):
    value = sum(lst[i])
    if max_value <= value:
        max_value = value
        max_index = i

print(max_index)