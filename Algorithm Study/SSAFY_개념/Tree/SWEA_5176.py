def in_order(v):
    global number
    if v <= N: # 전체크기보다 작을 때
        # 왼쪽
        in_order(2*v)
        Tree[v] = number
        number += 1
        # 오른쪽
        in_order(2*v+1)


T = int(input())

for tc in range(T):
    N = int(input())
    Tree = [0 for _ in range(N+1)]
    number = 1

    in_order(1)
    print("#{} {} {}".format(tc+1, Tree[1], Tree[N//2]))