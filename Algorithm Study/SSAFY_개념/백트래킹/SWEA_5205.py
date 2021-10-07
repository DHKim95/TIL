def quick_sort(array, start, end):
    # 왼쪽점이 오른쪽 점보다 클 경우
    if start >= end:
        return

    pivot = start # 피봇 점 지정
    left = start + 1 # 왼쪽 지점
    right = end # 오른쪽 지점

    while left <= right:
        # 배열 범위 내에서 피봇보다 큰 값을 찾을때까지 왼쪽 인덱스 움직이기
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 배열 범위 내에서 피봇보다 작은 값을 찾을때까지 오른쪽 인덱스 이동
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 왼쪽 오른쪽순서가 바뀌면 피봇과 오른쪽 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 값을 찾았을 경우 왼쪽과 오른쪽 교체
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1) # 피봇기준 왼쪽
    quick_sort(array, right + 1, end) # 피봇기준 오른쪽

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, len(arr) - 1)

    print("#{} {}".format(tc+1, arr[N//2]))