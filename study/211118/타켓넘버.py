numbers = [1,1,1,1,1]
target = 3

def dfs(idx, result, numbers, target):
    global answer # 전역변수 설정
    # idx가 전체 숫자가 되었을때
    if idx == len(numbers):
        # 타겟이 되면 한개 추가
        if result == target:
            answer += 1
        return
    # 모든 경우의 수 확인하기
    else:
        dfs(idx+1, result + numbers[idx], numbers, target)
        dfs(idx+1, result - numbers[idx], numbers, target)

answer = 0
def solution(numbers, target):
    dfs(0,0,numbers,target)

    return answer

print(solution(numbers, target))