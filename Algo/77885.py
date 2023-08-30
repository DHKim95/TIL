def solution(numbers):
    answer = []

    for number in numbers:

        bin_num = list('0' + bin(number)[2:])
        idx = ''.join(bin_num).rfind('0')  # 오른쪽부터 0 자리 찾기
        bin_num[idx] = '1'

        if number % 2 == 1:
            bin_num[idx + 1] = '0'

        answer.append(int(''.join(bin_num), 2))

    return answer