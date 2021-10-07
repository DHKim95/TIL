def merge_sort(array):
    # 만약 1개 이하이면 그대로 반환
    if len(array) <= 1:
        return array
    mid = len(array) // 2 # 중앙값
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

# def merge(left, right):
#     global cnt
#
#     # 오른쪽이 먼저 끝나면 +1 해준다.. 오른쪽 수가 더 작을경우 먼저 끝남..
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     result = []
#     # 왼쪽 오른쪽 한개이상 있으면
#     while len(left) > 0 or len(right) > 0:
#         # 둘다 존재할 때
#         if len(left) > 0 and len(right) > 0:
#             # 왼쪽이 크면
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             # 오른쪽이 크면
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#
#         # 한쪽만 존재할 때
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#     return result



def merge(left, right):
    global cnt

    # 오른쪽이 먼저 끝나면 +1 해준다.. 오른쪽 수가 더 작을경우 먼저 끝남..
    if left[-1] > right[-1]:
        cnt += 1

    result = [] # 결과창
    left_idx, right_idx = 0, 0
    # 왼쪽 오른쪽 한개이상 있으면
    while left_idx < len(left) or right_idx < len(right):
        # 둘다 존재할 때
        if left_idx < len(left) and right_idx < len(right):
            # 왼쪽
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            # 오른쪽
            else:
                result.append(right[right_idx])
                right_idx += 1

        # 한쪽만 존재할 때
        elif len(left) > left_idx:
            result.append(left[left_idx])
            left_idx += 1
        elif len(right) > right_idx:
            result.append(right[right_idx])
            right_idx += 1
    return result

T = int(input())

for tc in range(T):
    N = int(input()) # 정수 개수
    arr = list(map(int, input().split()))

    cnt = 0
    sort_arr = merge_sort(arr)

    print("#{} {} {}".format(tc+1, sort_arr[N//2], cnt))