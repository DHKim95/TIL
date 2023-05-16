from itertools import permutations

a, b = input().split()
b = int(b)
answer = -1

arr = []
for i in permutations(a):
    arr.append(''.join(i))

for i in arr:
    if i[0] == '0':
        continue
    i = int(i)
    if i < b:
        answer = max(answer, i)


print(answer)