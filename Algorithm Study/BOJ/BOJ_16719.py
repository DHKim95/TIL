def DFS(start, arr):
    if len(arr) == 0:
        return

    # 제일 작은 알파벳 찾기
    min_value = min(arr)
    now = arr.index(min_value)
    # 알파벳 만들기
    result[start + now] = min_value
    print("".join(result))
    # 찾은 위치에서 뒤쪽
    DFS(start+now+1, arr[now+1:])
    # 처음부터 현재까지
    DFS(start, arr[:now])

words = list(input())

if len(words) == 1:
    print(words[0])
# 한개가 아닐 경우
else:
    result = [""] * len(words)

    DFS(0, words)

