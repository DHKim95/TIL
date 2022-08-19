def solution(nums):
    num_len = len(set(nums))
    if len(nums) // 2 > num_len:
        return num_len
    else:
        return len(nums) // 2

print(solution([3,1,2,3]))