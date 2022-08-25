from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 쓸수있는 순서 만들기 -> 순열
    for p in permutations(dungeons, len(dungeons)):
        now = k
        cnt = 0

        # 최대로 할 수 있는 방법 생각하기
        for _min, _spend in p:
            if now >= _min:
                now -= _spend
                cnt += 1

        answer = max(answer, cnt)
    return answer