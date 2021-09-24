N = 3
arr = [1,2,3]
sel = [0] * N # 내가 직접 뽑은거 넣을 리스트
check = [0] * N # 내가 사용한거 체크할 리스트

# idx는 뽑고있는자리
# i는 체크자리

def perm(idx):
    if idx == N:
        print(sel)
    else:
        for k in range(N):
            if check[k] == 0:
                sel[idx] = arr[k]
                check[k] = 1 # 사용했다 -> 체크
                print("들어오는것",idx, k, sel, check)
                perm(idx+1)
                check[k] = 0 # 원상복귀
                print("나가는것", idx, k, sel, check)

perm(0)