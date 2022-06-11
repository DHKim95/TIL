N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

max_number = arr[-1]
second_number = arr[-2]

# cnt = 0
# while True:
#     # 횟수가 끝나면 종료
#     if M == 0:
#         break
#
#     # 한번에 최대로 더하는 만큼 더해주기
#     for i in range(K):
#         if M == 0:
#             break
#         cnt += max_number
#         M -= 1
#
#     # 두번째 수 한번 더하기
#     cnt += second_number
#     M -= 1
#
# print(cnt)

cnt = int(M / (K+1)) * K
cnt += M % (K+1)

result = 0
result += (cnt * max_number)
result += (M - cnt) * second_number

print(result)