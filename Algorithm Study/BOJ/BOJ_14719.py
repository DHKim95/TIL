# H는 세로, W는 가로
H, W = map(int, input().split())
block = list(map(int, input().split()))
cnt = 0

for i in range(1, W-1):
    # 기둥 설정
    left = max(block[:i])
    right = max(block[i+1:])
    diff = min(left, right)

    # 기둥 사이중 낮은 기둥 기점으로 차액 더하기
    if diff > block[i]:
        cnt += (diff - block[i])
print(cnt)