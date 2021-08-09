N = int(input())
lst = list(map(int, input().split(' ')))
sort_lst = sorted(lst)
print(sort_lst[N//2])