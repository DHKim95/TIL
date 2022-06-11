N = int(input())

cnt = 0
while True:
    # 5로 나누어지면 나누기
    if N % 5 == 0:
        cnt += N // 5
        break
    # 아닐 경우에 2씩 빼주면서 개수 더하기
    else:
        N -= 2
        cnt += 1

    if N < 0:
        break

if N >= 0:
    print(cnt)
else:
    print(-1)