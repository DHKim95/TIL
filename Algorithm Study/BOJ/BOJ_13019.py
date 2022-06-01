A = input()
B = input()

cnt = 0
now = len(A) - 1
check = False

if sorted(A) != sorted(B):
    check = True
    print(-1)

if check == True:
    pass
else:
    if now == 0:
        check = True
        if A == B:
            print(0)
        else:
            print(-1)

    if check == True:
        pass
    else:
        for i in range(len(A)-1, -1, -1):
            if A[i] != B[now]:
                cnt += 1
            else:
                now -= 1
        print(cnt)


