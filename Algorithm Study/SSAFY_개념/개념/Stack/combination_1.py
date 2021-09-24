# 순열은 순서가 상관있다.
# 조합은 순서가 상관없다.
N = 4
R = 2

arr = [1,2,3,4]
sel = [0] * R

# idx는 arr을 돈다
# s_idx는 sel을 돈다

def comb(idx, s_idx):
    # 여기 도달하면 다 뽑았음
    if s_idx == R:
        print(sel)
    elif idx == N:
        return

    else:
        sel[s_idx] = arr[idx]
        comb(idx+1, s_idx+1) # 해당 idx번째 자리를 뽑거나
        comb(idx+1, s_idx) # 해당 idx번째 자리를 뽑지않거나

comb(0,0)