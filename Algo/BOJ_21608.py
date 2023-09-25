N = int(input())

students = [list(map(int, input().split())) for _ in range(N**2)]
graph = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    my = student[0]
    like_student = student[1:]
    check_seat = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:

                like_cnt = 0
                empty_cnt = 0

                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] in like_student:
                            like_cnt += 1

                        if not graph[nx][ny]:
                            empty_cnt += 1

                # 자리 후보군 만들기
                check_seat.append((like_cnt, empty_cnt, i, j))

    # 자리 후보군 정렬
    check_seat = sorted(check_seat, key=lambda x: (-x[0], -x[1], x[2], x[3]))

    # 최적의 자리에 학생 앉히기
    graph[check_seat[0][2]][check_seat[0][3]] = my

students.sort()

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0

        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] in students[graph[i][j]-1]:
                cnt += 1

        # 점수기록
        if cnt != 0:
            answer += 10 ** (cnt - 1)

print(answer)
