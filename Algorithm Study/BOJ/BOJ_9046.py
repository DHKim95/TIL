N = int(input())

for _ in range(N):
    words = input()
    arr = [0] * 26
    for i in words:
        if i.isalpha():
            arr[ord(i)-ord('a')] += 1
    max_cnt = max(arr)

    if arr.count(max_cnt) > 1:
        print("?")
    else:
        print(chr(97 + arr.index(max_cnt)))