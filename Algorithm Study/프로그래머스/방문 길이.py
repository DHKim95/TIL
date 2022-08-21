def solution(dirs):
    x, y = 0, 0
    visited = []

    for d in dirs:
        if d == 'U' and y < 5:
            visited.append(((x, y), (x, y + 1)))
            y += 1

        elif d == 'D' and y > -5:
            visited.append(((x, y - 1), (x, y)))
            y -= 1

        elif d == 'R' and x < 5:
            visited.append(((x, y), (x + 1, y)))
            x += 1
        elif d == 'L' and x > -5:
            visited.append(((x - 1, y), (x, y)))
            x -= 1

    visited = set(visited)

    answer = len(visited)
    return answer