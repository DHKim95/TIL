word = input()
a_cnt = word.count('a')
answer = int(1e9)
left = 0

# 원형이기 때문에 만들어주기
while left < len(word):
    right = left + a_cnt
    if right > len(word):
        temp = word[left:len(word)] + word[:right-len(word)]
    else:
        temp = word[left:right]
    answer = min(answer, temp.count('b'))
    left += 1

print(answer)