def check(number):
    str_number = str(number)
    for k in range(len(str_number)-1):
        if str_number[k] > str_number[k+1]:
            return False
    return True

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = -1
    for i in range(len(arr)-1):
        for j in range(i+1, N):
            number = arr[i] * arr[j]
            if (answer < number) and check(number):
                answer = number

    print("#{} {}".format(tc+1, answer))