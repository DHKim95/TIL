def code(cnt):
    lst = [0] * N
    lst[0] = c_lst[0]
    for i in range(N-1):
        if lst[i] >= cnt:
            lst[i+1] = c_lst[i+1] + d_lst[i]
        elif lst[i] + d_lst[i] >= cnt:
            lst[i+1] = c_lst[i+1] + (lst[i]+d_lst[i]-cnt)
        else:
            return False
    if lst[N-1] >= cnt:
        return True
    else:
        return False


def search(start, end):
    if start == end:
        return start
    mid = (start+end+1) // 2
    if code(mid):
        return search(mid, end)
    else:
        return search(start, mid-1)

# N은 난이도 개수, T는 시나리오 개수
N, T = map(int, input().split())

for tc in range(T):

    c_lst = [0] * N
    d_lst = [0] * N
    # 2N-1개의 문제
    arr = list(map(int, input().split()))
    for i in range(N-1):
        c_lst[i] = arr[2*i]
        d_lst[i] = arr[2*i]
    c_lst[N-1] = arr[2*(N-1)]

    # print(c_lst)
    # print(d_lst)