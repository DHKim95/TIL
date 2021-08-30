T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split()) # N명 M초 K개
    arr = list(map(int, input().split()))
    arr.sort()

    answer = "Possible"
    for i in range(N):
        fish = (arr[i] // M) * K - (i+1)
        if fish < 0:
            answer = "Impossible"
            break

    print("#{} {}".format(tc+1, answer))


