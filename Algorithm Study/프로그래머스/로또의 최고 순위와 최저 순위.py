def solution(lottos, win_nums):
    cnt = 0
    zero = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            zero += 1

    # 당첨 최고
    max_cnt = cnt + zero
    lotto_rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    answer = [lotto_rank[max_cnt], lotto_rank[cnt]]
    return answer

print(solution([44,1,0,0,31,25], [31,10,45,1,6,19]))