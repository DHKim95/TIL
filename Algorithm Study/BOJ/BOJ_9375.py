T = int(input())

for _ in range(T):
    N = int(input())

    if N == 0:
        print(0)
        continue

    dic = dict()
    for _ in range(N):
        name, type = map(str, input().split())

        if type in dic.keys():
            dic[type] += 1
        else:
            dic[type] = 1

        answer = 1
        for key in dic.keys():
            answer *= dic[key] + 1

    print(answer - 1)