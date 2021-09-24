T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)] # 박스 N만큼 나열하기
    for i in range(1, Q+1):
        L, R = map(int, input().split()) # L, R입력받아서 인덱스가 한개 작으므로 -1을 해준 후 R까지 해당 수로 변환시키기
        for j in range(L-1, R):
            box[j]= i

    box = list(map(str, box)) # 한번에 출력을 하기 위해 문자열로 변경

    print("#{} {}".format(tc+1, ' '.join(box)))