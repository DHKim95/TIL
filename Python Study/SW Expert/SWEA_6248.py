words = list(input())
answer = ""
for i in range(len(words)):
    # 짝수번째만 놔두기
    if i % 2 == 0:
        answer += words[i]
        
print(answer)