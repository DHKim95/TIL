def DFS(words):
    global cnt

    arr = set(list(words))
    # 한개라면 종료
    if len(arr) == 1:
        cnt += 1
        return
    # 한개아니면 계속 줄이기
    else:
        DFS(words[1:])
        DFS(words[:-1])


N = input()
cnt = 0

DFS(N)
print(cnt)