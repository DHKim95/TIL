# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_cnt = 0
#
#     for i in range(N-1): # 리스트 한바퀴 돌기
#         cnt = 0
#         for j in range(i+1, N): # 한개씩 돌면서 나보다 작은 것은 낙차 하는것이기 때문에 +1을 해준다.
#             if arr[i] > arr[j]:
#                 cnt += 1
#         if max_cnt < cnt: # 최대값을 계속 갱신해준다.
#             max_cnt = cnt
#
#     print("#{} {}".format(tc + 1, max_cnt))


# 2차원
T = int(input()) # 테스트 케이스
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    graph = [[0] * max(arr) for _ in range(N)]

    for i in range(N): # 행
        for j in range(arr[i]): # 벽길이만큼 1로 표시해주기
            graph[i][j] = 1

    cnt_lst = []
    cnt = 0
    for row in range(N):
        for col in range(max(arr)):
            cnt = 0
            if graph[row][col] == 1:
                for m in range(row+1, N):
                    if graph[m][col] == 0:
                        cnt += 1
            cnt_lst.append(cnt)

    max_value = 0
    for num in cnt_lst:
        if num > max_value:
            max_value = num

    print("#{} {}".format(tc+1, max_value))
