T = int(input())
for tc in range(T):
    N, M = map(int, input().split()) # N은 정수의 개수, M은 구간의 개수
    arr = list(map(int, input().split()))
    lst = []

    for i in range(N-M+1):
        cnt = 0
        for j in arr[i:i+M]:
            cnt += j
        lst.append(cnt)

    print("#{} {}".format(tc+1, max(lst) - min(lst)))