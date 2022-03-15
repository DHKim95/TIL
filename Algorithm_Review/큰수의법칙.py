N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

first = arr[N-1]
second = arr[N-2]

answer = 0

while True:
    for i in range(K):
        if M == 0:
            break
        answer += first
        M -= 1
    if M == 0:
        break
    answer += second
    M -= 1

print(answer)