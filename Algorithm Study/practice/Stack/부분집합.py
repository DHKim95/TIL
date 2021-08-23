N = 3

sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
    else:
        # 뽑고 가고
        sel[idx] = 1
        powerset(idx+1)

        # 안뽑고가고
        sel[idx] = 0
        powerset(idx+1)

powerset(0)