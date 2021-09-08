N = int(input())

for i in range(N):
    check = False
    a_word, b_word = input().split()
    a_word = ''.join(sorted(a_word))
    b_word = ''.join(sorted(b_word))

    if len(a_word) != len(b_word):
        print("Impossible")
        continue

    for i in range(len(a_word)):
        if a_word[i] != b_word[i]:
            check = True
            break

    if check == True:
        print("Impossible")
    else:
        print("Possible")