T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    answer = 0

    # 문자열 비교(인덱스)
    for num in range(len(str2) - len(str1) + 1):
        if str1 == str2[num: num+len(str1)]:
            answer = 1

    # 간단한 방법
    # if str1 in str2:
    #     answer = 1

    print("#{} {}".format(tc+1, answer))
