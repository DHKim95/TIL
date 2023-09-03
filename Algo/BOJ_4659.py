word_check = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()

    cnt = 0
    check = False
    two_check = False

    if word == 'end':
        break

    # 모음 갯수 확인
    for i in word_check:
        if i in word:
            cnt += 1

    if cnt < 1:
        print(f"<{word}> is not acceptable.")
        continue

    # 3개 연속 확인
    for i in range(len(word)-2):
        if word[i] in word_check and word[i+1] in word_check and word[i+2] in word_check:
            check = True
        elif word[i] not in word_check and word[i+1] not in word_check and word[i+2] not in word_check:
            check = True
    if check:
        print(f"<{word}> is not acceptable.")
        continue

    # 같은 글자 연속2번 or ee&oo
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            two_check = True

    if two_check:
        print(f"<{word}> is not acceptable.")
        continue

    print(f"<{word}> is acceptable.")