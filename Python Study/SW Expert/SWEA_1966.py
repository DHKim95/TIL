T = int(input()) # 테스트 케이스 갯수
for i in range(T): 
    N = int(input()) # 숫자 갯수
    arr = list(map(int, input().split(' '))) # 리스트 입력받기
    arr_sort = list(map(str, sorted(arr))) # 정렬해서 문자열로 입력
    print(f'#{i+1} {" ".join(arr_sort)}')