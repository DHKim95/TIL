T = int(input())
for tc in range(T):
    circle = input()
    stick = 0 # 막대 개수
    cnt = 0 # 잘린 개수의 총합

    for i in range(len(circle)):
        # (일 경우 막대이니 1개 추가해준다.
        if circle[i] == "(":
            stick += 1
        # ) 일경우 레이저이거나 막대인 경우를 생각해준다.
        else:
            # 스틱을 없애주고
            stick -= 1
            # 만약 바로 전에꺼가 (일 경우 레이저이기 때문에 현재 스틱의 개수를 추가해준다.
            if circle[i-1] == "(":
                cnt += stick
            # (이게 아니라면 스틱의 끝이기 때문에 한개씩만 추가해준다.
            else:
                cnt += 1

    print("#{} {}".format(tc+1, cnt))