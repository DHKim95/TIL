N = int(input())

for i in range(N):
    lst = list(map(int, input().split(' ')))
    answer = round(sum(lst) / len(lst))

    print(f'#{i+1} {answer}')