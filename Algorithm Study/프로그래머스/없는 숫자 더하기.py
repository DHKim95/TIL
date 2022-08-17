def solution(numbers):
    arr = [i for i in range(10)]
    for num in numbers:
        arr[num] = 0
    answer = sum(arr)
    return answer

print(solution([1,2,3,4,6,7,8,0]))