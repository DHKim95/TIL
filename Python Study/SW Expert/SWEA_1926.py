N = int(input())
arr = [str(i) for i in range(1,N+1)]
lst = ["3","6","9"]
answer = []
for num in arr:
    cnt = 0 # 3, 6, 9가 몇개들어가는지 개수 세어주기
    for n in num: # 두자리수 이상일 경우 판단해주기
        if n in lst:
            cnt += 1
    if cnt != 0: # 한개 이상 들어가면 숫자를 추가
        answer.append(cnt)
    else: # 아닐경우 원래 숫자 추가
        answer.append(num)
        
for i in answer:
    if type(i) == str: # 문자열인 경우 원래 숫자기 때문에 그대로 출력
        print(i, end=' ')
    else: # 숫자일 경우 3,6,9가 포함된 것이기 때문에 숫자만큼 -로 표현
        print("-"*i, end=' ')


# 두번째로 푼것
# N = int(input())
# answer = []
# for i in range(1, N+1):
#     num = str(i)
#     if '3' in num or '6' in num or "9" in num:
#         answer.append( "-"*(num.count('3') + num.count('6') + num.count('9')))
#     else:
#         answer.append(i)
# print(*answer, end=' ')