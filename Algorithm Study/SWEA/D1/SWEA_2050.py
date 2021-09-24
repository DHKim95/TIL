words = input()
for word in words:
    print(ord(word) - 65 + 1, end=' ') # 아스키 코드 값 빼주기