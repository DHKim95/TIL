T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # M 횟수만큼 빼서 마지막에 넣어주기
    for i in range(M):
        arr.append(arr.pop(0))

    print("#{} {}".format(tc+1, arr[0]))