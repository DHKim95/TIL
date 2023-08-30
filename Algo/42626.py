import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        num = one + two * 2

        heapq.heappush(scoville, num)
        answer += 1

    if scoville[0] >= K:
        return answer
    return -1