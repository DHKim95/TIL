# 행 우선순회
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')

print()
# 열 우선 순회
for i in range(len(arr[0])):
    for j in range(len(arr)):
        print(arr[j][i], end=' ')

print()

# 지그재그 순회
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j + (3-1-2*j) * (i%2)], end=" ")
print()

for i in range(len(arr)):
    if i % 2 == 0:
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
    else:
        for j in range(len(arr[0])):
            print(arr[i][len(arr)-1-j], end=' ')
