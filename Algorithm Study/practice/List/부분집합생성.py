bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)

arr = [1,2,3]
N = len(arr)
for i in range(1<<N):
    for j in range(N+1):
        if i & (1<<j):
            print(arr[j], end=', ')
    print()
print()