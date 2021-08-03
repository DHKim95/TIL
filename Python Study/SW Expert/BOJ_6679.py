def two_change(x, number):
    if x < number: # X진법 이하면 그대로 반환해서 더한다.
        return int(x)
    else: # 계속 나누어주면서 더해준다.
        return two_change(x//number, number) + int(x % number) 

lst = [i for i in range(1000, 10000)]
answer = []
for num in lst: # 3가지 자릿수가 동일할 경우 정답 리스트에 추가
    if (two_change(num,10) == two_change(num, 12)) and (two_change(num, 12) == two_change(num, 16)):
        answer.append(num)
        
for i in answer:
    print(i)