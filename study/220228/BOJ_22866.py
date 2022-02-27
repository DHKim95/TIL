import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 갯수, 왼쪽 가까운거, 오른쪽 가까운거 -> 0으로 했다가 바꿈..
answer = [[0, -1, -1] for _ in range(N)]

left_lst = []
for i in range(N):
    # 존재할때 작거나 같으면 제거한다.
    while left_lst and arr[i] >= arr[left_lst[-1]]:
        left_lst.pop()
    # 기본적으로 추가
    left_lst.append(i)

    # print(left_lst)
    # 2개이상 들어가면 있는거기 때문에 넣어주기
    if len(left_lst) > 1:
        answer[i][0] += len(left_lst) - 1 # 더해줘야한다...
        answer[i][1] = left_lst[-2]

right_lst = []
for i in range(N-1, -1, -1):
    while right_lst and arr[i] >= arr[right_lst[-1]]:
        right_lst.pop()
    right_lst.append(i)

    if len(right_lst) > 1:
        answer[i][0] += len(right_lst) - 1
        answer[i][2] = right_lst[-2]

for i in range(N):
    # 0이 아니면
    if answer[i][0] == 0:
        print(0)
    else:
        # 둘다 있을 때
        if answer[i][1] != -1 and answer[i][2] != -1:
            # 더 가까운거 찾아서 출력하기
            if i - answer[i][1] <= answer[i][2] - i:
                print(answer[i][0], answer[i][1] + 1)
            else:
                print(answer[i][0], answer[i][2] + 1)


        elif answer[i][1] != -1:
            print(answer[i][0], answer[i][1] + 1)
        elif answer[i][2] != -1:
            print(answer[i][0], answer[i][2] + 1)




# # 번호 진행하기
# for i in range(N):
#
#     left_lst = [i]
#     for j in range(1, i+1):
#         # 보는것이 마지막 부분보다 높으면 그 위치 추가
#         if arr[i-j] > arr[left_lst[-1]]:
#             left_lst.append(i-j)
#
#     right_lst = [i]
#     for j in range(1, N-i):
#         if arr[i+j] > arr[right_lst[-1]]:
#             right_lst.append(i+j)
#
#     # 기존시작꺼 2개 빼주기
#     cnt = len(left_lst) + len(right_lst) - 2
#
#     if cnt > 0:
#         if len(left_lst) > 1:
#             print(cnt, left_lst[1] + 1)
#         elif len(right_lst) > 1:
#             print(cnt, right_lst[1] + 1)
#     elif len(left_lst) > 1:
#         print(cnt, left_lst[1] + 1)
#     elif len(right_lst) > 1:
#         print(cnt, right_lst[1] + 1)
#     else:
#         print(cnt)