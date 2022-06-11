N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
max_value = 0

for i in range(len(arr)):
    if max_value < arr[i] * (i+1):
        max_value = arr[i] * (i+1)

print(max_value)