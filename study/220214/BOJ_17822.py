from collections import deque

# N은 반지름, M은 숫자, T는 회전
N, M, T = map(int, input().split())

graph = deque(deque(map(int, input().split())) for _ in range(N))

# x의 배수인 원판을 d방향으로 k회전, d가 0이면 시계, 1이면 반시계

for _ in range(T):
    x, d, k = map(int, input().split())
