# T를 S로 고치기
def DFS(now):
    # S랑 같으면 1 반환
    if now == S:
        return 1

    # 길이가 더 작아버리면 0으로 반환
    if len(now) <= len(S):
        return 0

    cnt = 0
    # A로 끝나는 경우 A삭제
    if now[-1] == "A":
        cnt = DFS(now[:-1])

    if cnt == 1:
        return 1

    # B로 시작하는 경우는 뒤집어서 삭제
    if now[0] == "B":
        cnt = DFS(now[::-1][:-1])

    return cnt

S = input()
T = input()

cnt = DFS(T)
print(cnt)