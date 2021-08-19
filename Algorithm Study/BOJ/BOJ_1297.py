# D는 대각선 길이, H는 TV의 높이 비율, W는 TV의 너비비율
D, H, W = map(int, input().split())
length = D / ((H**2 + W**2) ** 0.5)
print(int(H * length), int(W * length))