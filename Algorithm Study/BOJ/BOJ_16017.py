a=int(input())
b=int(input())
c=int(input())
d=int(input())
check=0
if a==8 or a==9:
    if d==8 or d==9:
        if b==c:
            check=1
if check==1:
    print('ignore')
else:
    print('answer')