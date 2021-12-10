number_lst = {
    '0':[1,1,1,0,1,1,1],
    '1':[0,0,1,0,0,0,1],
    '2':[0,1,1,1,1,1,0],
    '3':[0,1,1,1,0,1,1],
    '4':[1,0,1,1,0,0,1],
    '5':[1,1,0,1,0,1,1],
    '6':[1,1,0,1,1,1,1],
    '7':[1,1,1,0,0,0,1],
    '8':[1,1,1,1,1,1,1],
    '9':[1,1,1,1,0,1,1],
    'x':[0,0,0,0,0,0,0]
}

T = int(input())

for tc in range(T):
    a, b = map(str, input().split())
    cnt = 0

    if len(a) == len(b):
        a_lst = list(a)
        b_lst = list(b)
    else:
        if len(a) < 5:
            a_lst = list(a.rjust(5, 'x'))
        elif len(a) == 5:
            a_lst = list(a)
        if len(b) < 5:
            b_lst = list(b.rjust(5, 'x'))
        elif len(b) == 5:
            b_lst = list(b)

    for i, j in zip(a_lst, b_lst):
        if i == 'x' and j == 'x':
            continue
        elif i == 'x' and j != 'x':
            x = number_lst[i]
            y = number_lst[j]
            sub_cnt = 0
            for k,l in zip(x,y):
                if k == l:
                    pass
                else:
                    sub_cnt += 1
            cnt += sub_cnt
        elif i != 'x' and j == 'x':
            x = number_lst[i]
            y = number_lst[j]
            sub_cnt = 0
            for k, l in zip(x, y):
                if k == l:
                    pass
                else:
                    sub_cnt += 1
            cnt += sub_cnt
        else:
            x = number_lst[i]
            y = number_lst[j]
            sub_cnt = 0
            for k, l in zip(x, y):
                if k == l:
                    pass
                else:
                    sub_cnt += 1
            cnt += sub_cnt

    print(cnt)