# 이진탐색으로 카운트 찾기
def page_search(target, left, right):
    cnt = 0
    while left <= right:
        mid = int((left+right)/2)
        if mid == target:
            break
        elif mid > target:
            right = mid
            cnt += 1
        else:
            left = mid
            cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split()) # 전체쪽수, A가 찾을 쪽수, B가 찾을 쪽수
    A_cnt = page_search(A, 1, P)
    B_cnt = page_search(B, 1, P)
    if A_cnt < B_cnt:
        answer = 'A'
    elif A_cnt > B_cnt:
        answer = 'B'
    else:
        answer = '0'


    print("#{} {}".format(tc+1, answer))