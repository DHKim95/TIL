import sys
input = sys.stdin.readline

N = int(input())
weight = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

weight.sort(reverse=True)
box.sort(reverse=True)

time_cnt = 0
# 옮길 수 있는지 확인하기
if max(box) > max(weight):
    print(-1)
else:
    # 박스가 없어질때까지
    while len(box) > 0:
        time_cnt += 1
        # 물건 옮기기
        for i in range(len(weight)):
            for j in range(len(box)):
                # 물건 제거
                if weight[i] >= box[j]:
                    box.pop(j)
                    break
    print(time_cnt)