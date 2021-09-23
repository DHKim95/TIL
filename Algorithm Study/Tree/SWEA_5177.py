# import heapq
#
# T = int(input()) # 테스트 케이스
# for tc in range(T):
#     N = int(input()) # 노드개수
#     arr = list(map(int, input().split()))
#     cnt = 0
#
#
#     print(arr)
#     # 숫자 맞춰주기
#     heapq.heapify(arr)
#     print(arr)
#
#     while N > 1:
#         N //= 2
#         cnt += arr[N-1]
#
#     print("#{} {}".format(tc+1, cnt))

T = int(input()) # 테스트 케이스
for tc in range(T):
    N = int(input()) # 노드개수
    arr = list(map(int, input().split()))
    Tree = [0] * (N+1)
    idx = 1 # 인덱스
    cnt = 0 # 합

    for i in arr:
        Tree[idx] = i
        sub_index = idx # sub_index 지정
        # 자식노드가 부모노드보다 클 경우 바꿔주기
        while Tree[sub_index] < Tree[sub_index // 2]:
            Tree[sub_index], Tree[sub_index//2] = Tree[sub_index//2], Tree[sub_index]
            sub_index //= 2 # 자식 계속 비교
        idx += 1

    while N > 1:
        N //= 2
        cnt += Tree[N]

    print("#{} {}".format(tc+1, cnt))
