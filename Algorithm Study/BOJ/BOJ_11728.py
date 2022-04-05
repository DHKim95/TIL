# N은 A의 크기, M은 B의 크기
N, M = map(int, input().split())

A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

answer = []
a_cnt, b_cnt = 0, 0
# 둘다 끝날때까지 계속 돈다
while a_cnt != len(A_arr) or b_cnt != len(B_arr):
    # 1번이 끝나면 2번만 계속 돈다
    if a_cnt == len(A_arr):
        answer.append(B_arr[b_cnt])
        b_cnt += 1
    # 2번이 끝나면 1번만 계속 돈다
    elif b_cnt == len(B_arr):
        answer.append(A_arr[a_cnt])
        a_cnt += 1
    # 한개라도 안끝났으면 차례대로 넣는다.
    else:
        if A_arr[a_cnt] < B_arr[b_cnt]:
            answer.append(A_arr[a_cnt])
            a_cnt += 1
        else:
            answer.append(B_arr[b_cnt])
            b_cnt += 1

print(*answer)