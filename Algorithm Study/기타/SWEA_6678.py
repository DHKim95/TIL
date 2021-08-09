# if문으로 풀었는데 입출력 Error가 떠서 try문으로 변경
while True:
    try:
        print(">> {}".format(input().upper()))
    except EOFError:
        break