import math

words = input()
word_len = len(words)

# 같은 문자열
if words == words[0] * word_len:
    print(-1)
elif words[math.ceil(word_len/2):] == words[:word_len // 2][::-1]:
    print(word_len-1)
else:
    print(word_len)