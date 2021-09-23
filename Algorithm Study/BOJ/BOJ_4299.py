_sum, _sub = map(int, input().split())

if _sum - _sub < 0 or (_sum - _sub) % 2 != 0:
    print(-1)
else:
    a = (_sum+_sub) // 2
    b = (_sum - a)

    print(max(a,b), min(a,b))