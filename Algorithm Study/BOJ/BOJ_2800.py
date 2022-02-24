from itertools import combinations

lst = list(map(str, input().strip()))
stack = []
position = []
answer = []

for idx, value in enumerate(lst):
    if value == '(':
        stack.append(idx)
    if value == ')':
        position.append((stack.pop(), idx))

for i in range(1, len(position)+1):
    comb_lst = combinations(position,i)
    for num in comb_lst:
        now = lst[:]
        for a, b in num:
            now[a] = ''
            now[b] = ''

        answer.append(''.join(now))

for i in sorted(set(list(answer))):
    print(i)