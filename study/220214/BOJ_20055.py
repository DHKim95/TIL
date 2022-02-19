from collections import deque

N, K = map(int, input().split())

# 내구도
arr = deque(list(map(int, input().split())))

# 로봇 여부
under_arr = deque([0] * N)
progress = 0 # 단계

while True:
    # 회전하기
    arr.rotate(1)
    under_arr.rotate(1)

    # 내려갈 위치에 로봇 내리기
    under_arr[-1] = 0

    # 로봇 움직이기
    for i in range(N-2, -1, -1):
        # 로봇이 없으면 넘어간다.
        if under_arr[i] == 0:
            continue

        # 다음칸에 로봇이 없고 내구도가 1이상이면 옮기고 내구도 감소
        if under_arr[i+1] == 0 and arr[i+1] > 0:
            arr[i+1] -= 1
            under_arr[i+1] = 1
            under_arr[i] = 0

    # 이동 후에 내리기
    under_arr[-1] = 0

    if arr[0] > 0 and under_arr[0] == 0:
        arr[0] -= 1
        under_arr[0] = 1

    progress += 1

    if arr.count(0) >= K:
        break

print(progress)