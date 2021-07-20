word = input() # 입력받기
reverse_word = word[::-1] # 문자 뒤집기

if word == reverse_word:
    print(reverse_word[::-1])
    print("입력하신 단어는 회문(Palindrome)입니다.")