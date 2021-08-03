T = int(input())
for i in range(T):
    scores = list(map(int, input().split())) # 점수 입력받기
    number = scores[0] # 첫번째 점수개수
    score_list = scores[1:] # 점수 리스트
    avg = sum(score_list) / (number) # 평균 구하기
    cnt = 0
    for score in score_list: # 평균을 넘는것만 찾아서 카운트하기
        if score > avg:
            cnt += 1
    
    print("{:.3f}%".format(cnt/number*100))