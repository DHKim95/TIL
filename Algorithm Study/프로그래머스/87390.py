# n^2 배열 자르기

def solution(n, left, right):
    answer = []
    for number in range(left, right+1):
        answer.append(max(number // n, number % n)+1)
    return answer