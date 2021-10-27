N, M = map(int, input().split())

card_lst = list(map(int, input().split()))
card_lst.sort() # 정렬

# 횟수만큼 더해주는데 계속 정렬시키기
for _ in range(M):
    # 제일작은 2개 더해서 반영시키기
    card_lst[0], card_lst[1] = card_lst[0] + card_lst[1], card_lst[0] + card_lst[1]
    card_lst.sort()

print(sum(card_lst))