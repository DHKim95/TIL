N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()
arr = []
for i in range(N-1):
    arr.append(sensor[i+1]-sensor[i])

arr.sort()
print(sum(arr[:N-K]))