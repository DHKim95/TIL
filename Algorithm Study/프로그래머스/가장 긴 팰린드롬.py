def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

def solution(s):
    answer = 0
    word_len = len(s)
    # 시작위치
    for i in range(word_len):
        # 글자수
        for j in range(i+1, word_len+1):
            # 길이 및 팰린드롬 조건 충족시 갱신
            if is_palindrome(s[i:j]) and (len(s[i:j]) > answer):
                answer = len(s[i:j])
    return answer