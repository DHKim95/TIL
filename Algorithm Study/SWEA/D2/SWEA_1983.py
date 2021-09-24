grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for tc in range(T):
    N, K = map(int, input().split()) # N은 학생수, K는 알고싶은 학생 번호

    scores = []
    for i in range(N):
        mid, fin, hw = map(int, input().split())

        scores.append(0.35*mid + 0.45*fin + 0.2*hw)

    result = [(score, idx+1) for idx, score in enumerate(scores)]
    result.sort(reverse=True)

    tmp = N//10
    answer = 0
    for i in range(N):
        if result[i][1] == K:
            ans = i // tmp

    print("#{} {}".format(tc+1, grades[ans]))