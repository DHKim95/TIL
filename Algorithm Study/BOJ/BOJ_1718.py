words = input()
word_key = input()
cnt, now = len(word_key), 0

for word in words:
    if word == ' ':
        print(' ', end='')
    else:
        pos = ord(word_key[now])-96
        if 97 <= ord(word)-pos <= 122:
            print(chr(ord(word) - pos), end='')
        else:
            print(chr(ord(word) - pos + 26), end='')
    now += 1
    if cnt <= now:
        now %= cnt