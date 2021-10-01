def Selectionsort(arr, idx):
    # 배열 길이
    N = len(arr)

    # 인덱스가 최종에 오면 끝
    if idx == N-1:
        return

    # 움직일 수 있는 인덱스 중에서 젤 왼쪽 인덱스
    min_num = idx
    for i in range(idx, N):

        # 작은 값을 찾아서 인덱스 갱신
        if arr[min_num] > arr[i]:
            min_num = i

    # 가장 작은 값과 바꿔주기
    arr[idx], arr[min_num] = arr[min_num], arr[idx]
    Selectionsort(arr, idx+1) # 한칸 이동동

arr = [5,8,4,6,2,3,1,7]
Selectionsort(arr, 0)
print(arr)