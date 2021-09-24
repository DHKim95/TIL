# 빈칸 기준 입력받기
word = list(map(str, input().split(' ')))

# 중복제거후 정렬
sort_word = sorted(list(set(word)))
print(','.join(sort_word))