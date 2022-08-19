from itertools import permutations

N = int(input())
arr = [i for i in range(1, N+1)]
answer = []

sort_arr = permutations(arr, N)
for i in sort_arr:
    print(*i)

