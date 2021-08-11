# 시간초과가 나지 않게 조심하자!

N = int(input())
arr = list(map(int, input().split()))
sort_arr = list(sorted(set(arr))) # 중복제거하고 정렬해서 다시 리스트로 만들어준다.
answer = {sort_arr[i]:i for i in range(len(sort_arr))}

for i in arr:
    print(answer[i], end=' ')