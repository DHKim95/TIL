import re

words = input()
s = re.compile('(100+1+|01)+')
x = s.fullmatch(words) # 일치여부 확인

if x:
    print("SUBMARINE")
else:
    print("NOISE")