T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # 뒤에서 N개 가져오기
    bin_num = bin(M)[2:][-N:]

    if len(bin_num) < N:
        print("#{} OFF".format(tc + 1))
    else:

        if '0' in bin_num:
            print("#{} OFF".format(tc+1))
        else:
            print("#{} ON".format(tc+1))