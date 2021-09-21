# import heapq
#
# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
#
# heap = []
# heapq.heapify(heap)
# for i in range(N):
#     for j in range(N):
#         heapq.heappush(heap, lst[i][j])
#         if len(heap) > N:
#             heapq.heappop(heap)
#
# print(heapq.heappop(heap))

N = int(input())
lst = list(map(int, input().split()))

for i in range(N-1):
    # 기존꺼랑 합치면서 계속 숫자가 높은것들만 정렬해서 추출한다.
    sort_lst = sorted(list(map(int, input().split())) + lst, reverse=True)
    lst = sort_lst[:N]

print(lst[N-1])