N = int(input())

for i in range(N):
    a, b = map(int, input().split(' '))
    if a > b:
        answer = ">"
    elif a < b:
        answer = "<"
    else:
        answer = "="

    print(f"#{i+1} {answer}")