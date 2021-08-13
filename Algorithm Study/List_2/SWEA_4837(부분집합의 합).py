T = int(input())
arr = [i for i in range(1, 13)]
len_arr = len(arr)
lst = []

# 부분집합 만들기
for i in range(1 << len_arr):
    sub_lst = []
    for j in range(len_arr+1):
        if i & (1<<j):
            sub_lst.append(arr[j])
    lst.append(sub_lst)



for tc in range(T):
    cnt = 0
    N, K = map(int, input().split())
    # 리스트를 돌면서 원소 수와 똑같은걸 찾으면
    for t in lst:
        if len(t) == N:
            hap = 0
            # 합을 구해서 target과 맞는지 확인한다.
            for k in t:
                hap += k
            if hap == K:
                cnt += 1

    print("#{} {}".format(tc+1, cnt))