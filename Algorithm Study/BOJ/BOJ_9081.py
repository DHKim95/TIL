N = int(input())

for _ in range(N):
    words = list(input())
    word_length = len(words)
    i = 0
    j = 1

    # 다음 가까운 단어 찾기
    for idx in range(1, word_length):
        if words[idx] > words[idx-1]:
            if i < idx:
                i = idx

    for idx in range(1, word_length):
        if words[idx] > words[i-1]:
            if j < idx:
                j = idx

    if i != 0 and j != 0:
        words[i-1], words[j] = words[j], words[i-1]

        words[i:] = list(reversed(words[i:]))
        # print(words)

    print(''.join(words))