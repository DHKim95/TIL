def solution(s):
    answer = s
    num_lst = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for number in num_lst.items():
        answer = answer.replace(number[0], str(number[1]))

    return int(answer)

print(solution("one4seveneight"))