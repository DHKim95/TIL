N = int(input())
arr = input()

color = {'B':0, 'R':0}
# 초기 세팅
color[arr[0]] += 1
# 변할때마다 색상
for i in range(1, N):
    if arr[i] != arr[i-1]:
        color[arr[i]] += 1

print(min(color['B'], color['R'])+1)