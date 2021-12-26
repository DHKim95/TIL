A_distance, B_distance, A_start, B_start = map(int, input().split())

A_lst = [A_start]
B_lst = [B_start]
answer = -1
cnt = 0

while True:
    A_start += A_distance
    B_start += B_distance
    A_lst.append(A_start)
    B_lst.append(B_start)
    if A_start in B_lst or B_start in A_lst:
        answer = min(A_start, B_start)
        break
    elif cnt > 1000:
        break
    cnt += 1

print(answer)