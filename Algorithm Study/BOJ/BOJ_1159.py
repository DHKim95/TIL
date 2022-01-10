N = int(input())
lst = []
for _ in range(N):
    lst.append(input()[0])

sort_lst = sorted(lst)
sort_set = set(sort_lst)
result = []

for i in sort_set:
    if sort_lst.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print("".join(sorted(result)))
else:
    print("PREDAJA")