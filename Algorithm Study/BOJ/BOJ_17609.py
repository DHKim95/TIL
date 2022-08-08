N = int(input())

for _ in range(N):
    words = input()

    left, right = 0, len(words)-1
    check = False
    while left < right:
        # 문자가 동일한경우
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            # 오른쪽 문자 제거 회문확인
            if left < right -1:
                now = words[:right] + words[right + 1:]
                if now[:] == now[::-1]:
                    check = True
                    print(1)
                    break

            # 왼쪽 문자 제거 회문확인
            if left + 1 < right:
                now = words[:left] + words[left + 1:]
                if now[:] == now[::-1]:
                    print(1)
                    check = True
                    break

            print(2)
            check = True
            break

    if not check:
        print(0)