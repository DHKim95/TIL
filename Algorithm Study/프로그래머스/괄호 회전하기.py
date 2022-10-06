from collections import deque

def rotate_check(words):
    stack = []
    for word in words:
        if word == '(' or word == '{' or word == '[':
            stack.append(word)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop()
            if word == ')' and x != '(':
                return False
            elif word == ']' and x != '[':
                return False
            elif word == '}' and x != '{':
                return False
    if len(stack) != 0:
        return False
    return True


def solution(s):
    words = deque(s) # rotate를 쓰기 위함
    answer = 0
    for i in range(len(words)):
        words.rotate(1) # 오른쪽으로 밀기
        
        if rotate_check(words):
            answer += 1
        
    return answer