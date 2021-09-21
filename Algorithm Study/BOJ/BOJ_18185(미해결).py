N = int(input())

arr = list(map(int, input().split()))
money = 0 # 구해야 하는 돈
idx = 0 # 인덱스

while idx < len(arr):

    # 첫번째에 없으면 넘어가기
    ramen = arr[idx]
    if ramen == 0:
        idx += 1
        continue

    # 3가지가 다 존재할 때
    if len(arr) - idx > 2:
        ramen2 = arr[idx+1]
        ramen3 = arr[idx+2]

        #
        if ramen2 > ramen3:
            number = min(ramen, ramen2 - ramen3)

        num = min(ramen, ramen2, ramen3)
        ramen -= num
        ramen2 -= num
        ramen3 -= num


    elif len(arr) - idx > 1:
        pass

    else:
        pass
