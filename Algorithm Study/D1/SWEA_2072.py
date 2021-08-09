N = int(input()) # 테스트 케이스

for i in range(N):
    arr = list(map(int, input().split(' '))) #빈 칸 기준으로 입력 받아서 리스트로 만들기
    # 필터를 통해 홀수만 찾아 합하기
    answer = sum(list(filter(lambda x: x % 2 == 1, arr)))

    print(f"#{i+1} {answer}")