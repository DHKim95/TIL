name = "BBB"

def solution(name):
    answer = 0 # 횟수 더하기

    # 왼쪽이 큰지 오른쪽으로 가는게 큰지 확인해서 최솟값 더하기
    for i in name:
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)

    # 리스트로 바꿔주고 지나간것은 A로 변환
    name = list(name)
    name[0] = 'A'

    print(answer)
    for i in range(len(name)):
        # A일 경우 건너뛰기
        if name[i] == 'A':
            continue

        # 왼쪽 오른쪽 이동 횟수
        left, right = 1, 1

        print(i, name)
        # 왼쪽으로
        while name[i - left] == 'A':
            print('왼쪽', left)
            left += 1

        while i + right <= len(name) - 1 and name[i + right] == 'A':
            print("오른쪽", right)
            right += 1

        if left < right:
            answer += left
        else:
            answer += right
        name[i] = 'A'

    return answer

print(solution(name))