N, K = map(int, input().split())

arr = []
for i in range(1, K+1):
    arr.append(N*i)

rev_arr = []
for i in arr:
    num = ""
    for k in range(len(str(i))-1, -1, -1):
        num += str(i)[k]

    rev_arr.append(int(num))

print(max(rev_arr))