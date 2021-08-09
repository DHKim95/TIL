calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

N = int(input())

for i in range(N):
    calen = input()
    year = calen[:4]
    month = calen[4:6]
    day = calen[6:8]
    if 1<= int(month) <= 12:
        if 1<= int(day) <= calendar[int(month)-1]:
            answer = f"{year}/{month}/{day}"
        else:
            answer = -1
    else:
        answer = -1
    
    print(f"#{i+1} {answer}")