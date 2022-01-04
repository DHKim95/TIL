a, b, c = map(int, input().split())

lst = [a, b, c, a*b, a*c, b*c, a*b*c]
sort_lst = sorted(lst, reverse=True)

cnt = sort_lst[0]
for num in sort_lst:
    if num % 2 == 1:
        cnt = num
        break
    else:
        if cnt < num:
            cnt = num

print(cnt)