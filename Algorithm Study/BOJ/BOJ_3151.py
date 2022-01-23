from collections import Counter
N = int(input())

arr = list(map(int, input().split()))
arr.sort()
new_arr = Counter(arr)
cnt = 0

# 학생 돌리기
for idx, value in enumerate(arr):
    # 시작과 끝
    start, end = idx+1, N-1
    while start < end:
        _sum = arr[start] + arr[end] + arr[idx]
        # 합이 0일 경우
        if _sum == 0:
            if arr[start] == arr[end]:
                cnt += (end - start)
            else:
                cnt +=  new_arr[arr[end]]
            start += 1
        # 총합이 0보다 큰경우
        elif _sum > 0:
            end -= 1
        # 총합이 0보다 작은경우
        elif _sum < 0:
            start += 1

print(cnt)