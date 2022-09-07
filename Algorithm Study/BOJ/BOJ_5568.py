from itertools import permutations

N = int(input())
K = int(input())

card = []
answer = []
for _ in range(N):
    card.append(input())

for i in permutations(card, K):
    answer.append(''.join(i))

print(len(set(answer)))