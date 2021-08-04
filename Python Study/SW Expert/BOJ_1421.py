N, C, W = map(int, input().split()) # N은 나무의 개수, C는 자르는 비용, W는 나무 한단위 가격
wood_list = []
for i in range(N):
    wood = int(input())
    wood_list.append(wood)

for num in range(1, max(wood_list)):
    cnt = 0


103 -> 1로 자르면 103 -> 1030