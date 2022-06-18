import sys

input = sys.stdin.readline
# N은 원생의 수, K는 조의 개수,
N, K = map(int, input().split())

arr = list(map(int, input().split()))

cost = []
for i in range(N-1):
    cost.append(arr[i+1] - arr[i])

cost.sort()
print(sum(cost[:N-K]))