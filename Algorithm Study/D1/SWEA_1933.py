# SWEA 1933 간단한 N의 약수
N = int(input())
answer = []
for i in range(1, N+1):
    if N % i == 0:
        answer.append(str(i))
        
print(" ".join(answer))