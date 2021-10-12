def DFS(idx, height):
    global min_num
    # B와 크거나 같고 최소값보다 작으면 갱신
    if B <= height < min_num:
        min_num = height
    if idx == N:
        return

    # 인덱스를 포함안하는 경우
    DFS(idx+1, height)
    # 인덱스를 포함하는 경우
    DFS(idx+1, height + h_lst[idx])

T = int(input())

for tc in range(T):
    N, B = map(int, input().split()) # N명 직원, 선반 높이
    h_lst = list(map(int, input().split())) # 각 점원의 키

    min_num = 999999999 # 임의 지정
    DFS(0,0)

    print("#{} {}".format(tc+1, min_num - B))