N = int(input())
p_number = []
n_number = []
max_number = 0

for _ in range(N):
    number = int(input())

    if number > 1:
        p_number.append(number)
    elif number == 1:
        max_number += 1
    else:
        n_number.append(number)

p_number.sort(reverse=True)
n_number.sort()

if len(p_number) % 2 == 0:
    for i in range(0,len(p_number), 2):
        max_number += p_number[i] * p_number[i+1]
else:
    for i in range(0,len(p_number)-1, 2):
        max_number += p_number[i] * p_number[i+1]
    max_number += p_number[len(p_number)-1] # 마지막 수

if len(n_number) % 2 == 0:
    for i in range(0,len(n_number), 2):
        max_number += n_number[i] * n_number[i+1]
else:
    for i in range(0,len(n_number)-1, 2):
        max_number += n_number[i] * n_number[i+1]
    max_number += n_number[len(n_number)-1]

print(max_number)