# 풀었는데 파이썬이 없음

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dic = {}

    for i in arr:
        number = abs(i)
        if number in dic:
            dic[number] += 1
        else:
            dic[number] = 1

    sort_dic = sorted(dic.items())

    print("#{} {} {}".format(tc+1, sort_dic[0][0], sort_dic[0][1]))