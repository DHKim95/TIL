T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(str, input().split()))

    left_arr = arr[:(N+1)//2]
    right_arr = arr[(N+1)//2:]
    answer = []

    if N % 2 == 0:
        for i in range(len(left_arr)):
            answer.append(left_arr[i])
            answer.append(right_arr[i])
    else:
        for i in range(len(left_arr)-1):
            answer.append(left_arr[i])
            answer.append(right_arr[i])
        answer.append(left_arr[-1])

    print("#{}".format(tc+1), end=' ')
    for i in answer:
        print(i, end=' ')
    print()

