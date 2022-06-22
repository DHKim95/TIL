number = input()
cnt = 0

for i in range(len(number)-1):
    if number[i] != number[i+1]:
        cnt += 1

print((cnt + 1) // 2)