T = int(input())

for _ in range(T):
    lst = [0,0]
    for _ in range(int(input())):
        a, b = input().split()
        if a == 'R' and b == 'P':
            lst[1] += 1
        elif a == 'R' and b == 'S':
            lst[0] += 1
        elif a == 'P' and b == 'R':
            lst[0] += 1
        elif a == 'P' and b == 'S':
            lst[1] += 1
        elif a == 'S' and b == 'P':
            lst[0] += 1
        elif a == 'S' and b == 'R':
            lst[1] += 1
    if lst[0] > lst[1]:
        print("Player 1")
    elif lst[0] == lst[1]:
        print("TIE")
    elif lst[0] < lst[1]:
        print("Player 2")