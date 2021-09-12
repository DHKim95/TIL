# 투포인터로 풀지 않으면 시간 초과가 뜬다.
# 이분탐색도 가능하다.

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    N.sort(reverse=True)
    M.sort(reverse=True)

    cnt = 0
    a_index = 0
    b_index = 0
    while a_index < A and b_index < B:
        if N[a_index] > M[b_index]:
            cnt += B - b_index
            a_index += 1
        else:
            b_index += 1

    print(cnt)