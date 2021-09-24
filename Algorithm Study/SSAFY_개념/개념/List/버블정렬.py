arr = [54, 28, 31, 5, 9, 2]

# 끝에서부터 순차적으로 내려온다.
for i in range(len(arr)-1, 0, -1):
    # 앞에서부터 큰 것이 있으면 뒤로 보내준다.
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)