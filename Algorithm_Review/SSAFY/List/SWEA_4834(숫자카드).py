T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))
    number_lst = [0 for _ in range(10)]

    for num in arr:
        number_lst[num] += 1

    max_value = 0
    max_index = 0
    for i in range(len(number_lst)):
        if number_lst[i] >= max_value:
            max_value = number_lst[i]
            max_index = i

    print("#{} {} {}".format(tc+1, max_index , max_value))
