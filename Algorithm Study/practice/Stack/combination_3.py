# 3개 정도는 반복문으로도 짜기 가능

N = 4
arr = [1,2,3,4]

# 인덱스 확인 잘하기
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])