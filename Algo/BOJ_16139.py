word = input()
N = int(input())

arr = [[0] * 26 for _ in range(len(word)+1)]

for i in range(1, len(word)+1):
    for j in range(26):
        if ord(word[i-1])-97 == j:
            arr[i][j] = arr[i-1][j] + 1
        else:
            arr[i][j] = arr[i-1][j]

for _ in range(N):
    alpha, start, end = input().split()
    alpha, start, end = ord(alpha)-97, int(start), int(end)

    print(arr[end+1][alpha] - arr[start][alpha])