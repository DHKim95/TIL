def solution(data, col, row_begin, row_end):
    # col번째 오름차순 정렬을 그 값이 동일하면 기본키인 첫 번째 컬럼으로 내림차순 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    answer = 0

    # 정렬된 데이터에서 S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    for i in range(row_begin - 1, row_end):
        sub_cnt = 0
        for a in data[i]:
            sub_cnt += (a % (i + 1))

        # 누적 XOR
        answer = answer ^ sub_cnt

    return answer



data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

print(solution(data, col, row_begin, row_end))