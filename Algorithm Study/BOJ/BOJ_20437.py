T = int(input())
for _ in range(T):
    W = list(map(lambda x: ord(x) - 97, input()))
    K = int(input())
    back = len(W)
    front = -1

    # 알파리스트
    alpha_list = [[] for _ in range(26)]
    # 같은 알파벳끼리 묶어주기
    for idx, value in enumerate(W):
        alpha_list[value].append(idx)

    # 2개씩 돌면서 문자열 찾기
    for alpha in alpha_list:
        for i in range(len(alpha) - K + 1):
            back = min(back, alpha[i + K -1] - alpha[i] + 1)
            front = max(front, alpha[i + K - 1] - alpha[i] + 1)

    if front == -1:
        print(-1)
    else:
        print(back, front)
