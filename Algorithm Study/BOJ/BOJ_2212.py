N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

arr = []
for i in range(1, N):
    arr.append(sensor[i] - sensor[i-1])

arr.sort()

print(sum(arr[:N-K]))