N = int(input())
arr = list(map(int, input().split()))
a, b = divmod(sum(arr), 3)
cnt = 0

if b == 0:
    # 물뿌리개 횟수 구하기
    for i in arr:
        cnt += (i // 2)

        
    if cnt >= a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
