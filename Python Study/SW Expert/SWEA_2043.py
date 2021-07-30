P, K = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    if P == K:
        break
    else:
        K += 1
        
print(cnt)