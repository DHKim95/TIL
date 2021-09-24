arr = [[1,2,3],[4,5,6],[7,8,9]]

dx = [0,0,-1, 1]
dy = [-1, 1, 0, 0]
x,y = 1, 1
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print()
        for k in range(4):
            print(arr[x+dx[k]][y+dy[k]], end=' ')
