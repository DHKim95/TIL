numbers = [6, 10, 2]

def solution(numbers):
    # 전부 문자열로 변환시키기
    numbers = list(map(str, numbers))
    # 3자리수 맞추기 위해 *3을 해서 맞춘다. 정렬은 큰 순으로
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 나머지 숫자 전부 합치기
    return str(int(''.join(numbers)))

print(solution(numbers))
