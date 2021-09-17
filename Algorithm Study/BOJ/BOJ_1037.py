N = int(input())

arr = list(map(int, input().split()))
max_number = max(arr)
min_number = min(arr)
print(max_number * min_number)