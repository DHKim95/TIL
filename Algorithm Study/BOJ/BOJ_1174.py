def DFS():
    if len(arr) > 0:
        result.add(int("".join(map(str, arr))))

    for i in range(10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            DFS()
            arr.pop()

N = int(input())

arr = []
result = set()

try:
    DFS()
    result = list(result)
    result.sort()
    print(result[N-1])
except:
    print(-1)