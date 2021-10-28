# from itertools import combinations
#
# while True:
#     arr = list(map(int, input().split()))
#     if arr[0] == 0:
#         break
#     arr = arr[1:]
#     comb_lst = list(combinations(arr, 6))
#
#     for i in comb_lst:
#         for j in i:
#             print(j, end=' ')
#         print()
#     print()
#####################################################
def DFS(idx, num):
    # 6개가 되었을 때 계속 출력
    if idx == 6:
        for i in range(6):
            print(comb_lst[i], end=' ')
        print()
        return

    # 전체를 탐색하기
    for i in range(num, len(arr)):
        comb_lst[idx] = arr[i]
        DFS(idx+1, i+1)

comb_lst = [0 for _ in range(6)] # 6칸
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    DFS(0,0)
    print()