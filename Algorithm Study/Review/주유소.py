N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = road[0] * price[0]
min_value = price[0]

for i in range(1, N-1):
    if min_value > price[i]:
        min_value = price[i]

    min_price += min_value * road[i]

print(min_price)