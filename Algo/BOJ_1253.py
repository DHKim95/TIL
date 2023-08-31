N = int(input())

arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(N):
    # 구하는 수 빼주기 -> 제거는안됨..
    arr_now = arr[:i] + arr[i+1:]
    start = 0
    end = len(arr_now)-1
    check_num = arr[i]

    while start < end:
        cnt = arr_now[start] + arr_now[end]
        if check_num == cnt:
            answer += 1
            break
        elif check_num > cnt:
            start += 1
        else:
            end -= 1

print(answer)