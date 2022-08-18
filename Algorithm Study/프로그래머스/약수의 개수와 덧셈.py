def solution(left, right):
    def check(number):
        arr = []
        for i in range(1, number + 1):
            if number % i == 0:
                arr.append(i)
        return len(arr)

    answer = 0
    for num in range(left, right + 1):
        if check(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer