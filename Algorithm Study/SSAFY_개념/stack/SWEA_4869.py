def paper(N):  # 크기 일치시 1개 추가
    if N == 20: # 정사각형 종이이므로 3개가 나올 수 있다.
        return 3
    elif N == 10:  # 한개밖에 나오지 못한다.
        return 1
    return paper(N - 10) + (paper(N - 20) * 2)

T = int(input())
for tc in range(T):
    N = int(input())  # 가로의 길이

    print("#{}".format(tc + 1), paper(N))