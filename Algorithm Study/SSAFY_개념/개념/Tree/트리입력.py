# 6
# 1 2 1 3 2 4 3 5 3 6

def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)


V = int(input())
edge = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1)
right = [0] * (V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

cnt = 0
pre_order(1)
print(cnt) # 3을 루트로 하는 서브트리의 정점 수
print(cnt - 1) # 3의 자손의 수