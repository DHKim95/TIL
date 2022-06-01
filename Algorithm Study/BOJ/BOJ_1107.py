target = int(input())
N = int(input())

if N == 0:
    arr = set()
else:
    arr = list(map(int, input().split()))

min_cnt = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        # 고장났으면 break
        if int(nums[j]) in arr:
            break

        # 고장난 숫자 없이 마지막 자리 왔으면 비교
        elif j == len(nums)-1:
            min_cnt = min(min_cnt, abs(int(nums) - target) + len(nums))

print(min_cnt)