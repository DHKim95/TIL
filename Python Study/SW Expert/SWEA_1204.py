T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = [0 for _ in range(max(arr)+1)] # 제일 큰 수 까지 0으로 리스트 만들기
    for num in arr: # 해당 숫자만큼 + 1해주기
        lst[num] += 1
    
    answer = [] # 정답 리스트
    for number in range(len(lst)): # 인덱스로 회전
        if lst[number] == max(lst): # 빈도수가 가장 높은 숫자의 인덱스를 찾아 정답 리스트에 추가
            answer.append(number) 
    
    print(f"#{i+1} {max(answer)}") # 높은것 중 가장 큰 수 반환