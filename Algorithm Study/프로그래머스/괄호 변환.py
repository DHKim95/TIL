

def solution(p):
    answer = ''
    
    # 빈문자열인 경우 반환
    if len(p) == 0:
        return p

    def split_word(p):
        open_p, close_p = 0, 0
        for i in range(len(p)):
            if p[i] == '(':
                open_p += 1
            else:
                close_p += 1
            if open_p == close_p:
                return p[:i+1], p[i+1:]
    
    # 2번
    u, v = split_word(p)
    
    def checkword(u):
        stack = []
        for word in u:
            if word == '(':
                stack.append(word)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return True
    
    # 3번
    if checkword(u):
        return u + solution(v)
    # 4번
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        for word in u[1:-1]:
            if word == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer
    
    return answer