def babygin(player, number):
    # 트리플인 경우
    if player[number] == 3:
        return True
    # 왼쪽으로 run
    elif number > 2 and player[number-1] and player[number-2]:
        return True
    # 양쪽으로 run
    elif 1 < number < 9 and player[number-1] and player[number+1]:
        return True
    # 오른쪽으로 run
    elif number < 8 and player[number+1] and player[number+2]:
        return True
    return False

T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))

    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    answer = 0

    for i in range(len(arr)):

        if i % 2 == 0:
            player1[arr[i]] += 1
            if babygin(player1, arr[i]):
                answer = 1
                break
        else:
            player2[arr[i]] += 1
            if babygin(player2, arr[i]):
                answer = 2
                break

    print("#{} {}".format(tc+1, answer))