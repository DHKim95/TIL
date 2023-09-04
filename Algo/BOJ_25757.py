N, game = map(str, input().split())
N = int(N)
check = 0

if game == 'Y':
    check = 2
elif game == 'F':
    check = 3
elif game == 'O':
    check = 4

member = set()
cnt = 1
answer = 0

for _ in range(N):
    name = input()

    if name not in member:
        member.add(name)
        cnt += 1
        if cnt == check:
            cnt = 1
            answer += 1

print(answer)