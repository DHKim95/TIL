# PyPy

N = int(input())
cra = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

cnt = 0
cra.sort(reverse=True)
weight.sort(reverse=True)

# 못옮기는 경우
if cra[0] < weight[0]:
    print(-1)
else:
    while len(weight) > 0:
        for c in cra:
            for w in weight:
                if c >= w:
                    weight.remove(w)
                    break

        cnt += 1

    print(cnt)