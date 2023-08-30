N, M = map(int, input().split())

answer = 0
checklist = []
for _ in range(N):
    checklist.append(input())

for _ in range(M):
    words = input()
    if words in checklist:
        answer += 1

print(answer)