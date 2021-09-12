N = int(input())

dic = {}

for _ in range(N):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# value와 key를 바꿔서 value를 가장 높은거를 찾아서 키값을 출력
new_dic = dict([(value, key) for key, value in dic.items()])

print(new_dic[max(new_dic.keys())])