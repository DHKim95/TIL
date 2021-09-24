def in_order(v):
    if len(arr[v]) >= 3:
        in_order(int(arr[v][2]))

    print(arr[v][1], end="")

    if len(arr[v]) == 4:
        in_order(int(arr[v][3]))


for tc in range(1, 11):
    N = int(input())

    arr = [[]]

    for i in range(N):
        arr.append(input().split())

    print("#{}".format(tc), end=" ")
    in_order(1)
    print()