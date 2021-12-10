# M은 코드 수, N은 전체 수, K는 숫자
M, N, K = map(int, input().split())

secret_code = list(map(int, input().split()))
lst = list(map(int, input().split()))

check = False
if M == N:
    if secret_code[:] == lst[:]:
        check = True
else:
    for i in range(N-M):
        if secret_code[:] == lst[i:i+M]:
            check = True

if check == True:
    print("secret")
else:
    print("normal")