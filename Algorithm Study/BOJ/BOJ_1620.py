import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # rstrip 필요

dic = {}
for i in range(1, N+1):
    poke = input().rstrip()
    dic[poke] = str(i)
    dic[str(i)] = poke
    
for _ in range(M):
    print(dic[input().rstrip()])