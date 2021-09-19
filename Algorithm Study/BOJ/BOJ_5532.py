L = int(input()) # 방학일수
A = int(input()) # 국어 총 페이지
B = int(input()) # 수학 총 페이지
C = int(input()) # 국어 최대 페이지
D = int(input()) # 수학 최대 페이지

if A % C == 0:
    a = A // C
else:
    a = (A // C) + 1

if B % D == 0:
    b = B // D
else:
    b = (B // D) + 1

cnt = max(a, b)

print(L-cnt)