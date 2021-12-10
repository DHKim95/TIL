N, M = map(int, input().split())

plan = [0 for _ in range(100)] # 계획
lst = [0 for _ in range(100)] # 실제주행
check = 0 # 리스트 체크 변수

# 100층밖에 안되기 때문에 구간별 속도 구현해주기
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(check,a+check):
        plan[i] = b
    check += a

# 실제주행 리스트 구현해주기
check = 0
for _ in range(M):
    a, b = map(int, input().split())
    for i in range(check, a + check):
        lst[i] = b
    check += a

max_value = 0
# 차이를 계산해 가장 차이가 큰 값 선정
for i in range(100):
    x = lst[i] - plan[i]
    if max_value < x:
        max_value = x

print(max_value)