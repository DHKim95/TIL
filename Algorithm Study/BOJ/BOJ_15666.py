from itertools import combinations_with_replacement

N, M = map(int, input().split())

arr = list(set(map(int, input().split())))
arr.sort()

lst = list(combinations_with_replacement(arr, M))
for i in lst:
    print(*i)