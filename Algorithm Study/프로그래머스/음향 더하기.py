def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign == True:
            answer += (num * 1)
        else:
            answer += (num * -1)
    return answer
