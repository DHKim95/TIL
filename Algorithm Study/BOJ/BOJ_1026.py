N = int(input())

A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

cnt = 0
# 가장 작은 값과 가장 큰 값을 곱하는게 제일 최소
for _ in range(N):
    cnt += A_lst.pop(A_lst.index(min(A_lst))) * B_lst.pop(B_lst.index(max(B_lst)))

print(cnt)
