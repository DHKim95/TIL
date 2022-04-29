N = int(input())

cow_lst = [-1] * 10
cnt = 0

for i in range(N):
    cow_num, direction = map(int, input().split())
    # 이전 위치 저장
    prev_idx = cow_lst[cow_num - 1]
    # 소 표시
    cow_lst[cow_num - 1] = direction

    # 이전 위치와 현재 위치가 다르면 추가
    if prev_idx != -1 and prev_idx != direction:
        cnt += 1

print(cnt)