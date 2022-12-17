def solution(grid):
    
    def move(x, y, direction, position):
        # 방향따라 방향 바꾸기
        if position == 'L':
            direction = (direction - 1) % 4
        elif position == 'R':
            direction = (direction + 1) % 4
        
        # 새로운 좌표 
        nx = (x + dx[direction]) % height
        ny = (y + dy[direction]) % width
        
        return nx, ny, direction
    
    height = len(grid)
    width = len(grid[0])
    
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    answer = []
    visited = [[[0] * 4 for _ in range(width)] for _ in range(height)]
    
    
    for i in range(height):
        for j in range(width):
            for d in range(4):
                if visited[i][j][d] == 0:
                    cnt = 0
                    x, y, direction = i, j, d
                    
                    while visited[x][y][direction] == 0:
                        cnt += 1
                        visited[x][y][direction] = 1 # 방문처리
                        x, y, direction = move(x, y, direction, grid[x][y])
                    
                    answer.append(cnt)
    
    
    # 아 정렬...;;
    answer.sort()
    return answer