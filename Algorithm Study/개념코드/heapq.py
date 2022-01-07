import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소 차례대로 삽입
    for value in iterable:
        heapq.heappush(h, value)
        # print(h)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
        print(h)
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)