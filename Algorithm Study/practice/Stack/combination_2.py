N = 4
R = 2

arr = [1,2,3,4]
sel = [0] * R

# idx는 arr을 시작하는 위치
# s_idx는 내가 뽑고있는 위치

def comb(idx, s_idx):
    if s_idx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[s_idx] = arr[i]
        comb(i+1, s_idx+1)

comb(0, 0)