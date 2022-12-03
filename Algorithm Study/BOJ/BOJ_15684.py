N, M, H = map(int, input().split())
# N은 세로선(열)개수 , M은 사다리 개수, H는 가로줄 칸 개수

# 사다리 만들기
graph = [[0] * N for _ in range(H)]

# 선 추가
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

# 출력선 확인하기
def check():
    for i in range(N):
        now = i
        for j in range(H):
            if graph[j][now] == 1:
                now += 1
            # now가 왼쪽으로 갈 수 있는 경우
            elif now > 0 and graph[j][now-1]:
                now -= 1

        # 세로 끝까지 다왔는데 원래 길과 다를 때
        if now != i:
            return False
    # 모든선이 다 제자리로 찾아간다면 True반환
    return True


def DFS(cnt, idx, limit):
    global answer
    # 갯수를 초과할 때
    if answer < cnt:
        return

    # 제한갯수일때
    if cnt == limit:
        # 출력이 제대로 나오는지 확인하기
        if check():
            answer = min(answer, cnt)
            return
        ## 너가 문제ㅔㄴ..
        else:
            return False

    # 이어서 사다리 만들기
    for i in range(idx, H):
        # 세로 확인하기
        for j in range(N-1):
            # 사다리를 못놓는 경우
            if graph[i][j] == 1:
                continue

            # 사다리를 놓을 수 있는 경우인데 못놓는 경우
            if graph[i][j] == 0:
                # 왼쪽에 사다리가 있는 경우
                if j -1 >= 0 and graph[i][j-1] == 1:
                    continue
                # 오른쪽에 사다리가 있는 경우(오른쪽없고 인덱스가 0번이라 -2)
                if j + 1 <= N - 2 and graph[i][j+1] == 1:
                    continue

            # 사다리 긋기
            graph[i][j] = 1

            DFS(cnt + 1, i, limit)
            # 사다리 없애기
            graph[i][j] = 0

answer = 987654321
# cnt, 가로선(행)
for limit in range(4):
    if DFS(0, 0, limit):
        break
if answer != 987654321:
    print(answer)
else:
    print(-1)