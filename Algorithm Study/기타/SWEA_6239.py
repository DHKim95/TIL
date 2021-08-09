# 빈칸 기준 리스트로 입력받기
word = list(map(str, input().split(' ')))
reverse_word = word[::-1]

# 뒤집엇 뒤에서 부터 출력
for i in reverse_word[:-1]:
    print(i, end=' ')
print(reverse_word[-1])