words = input()
lst = ['pi', 'ka', 'chu']

for i in lst:
    words = words.replace(i, ' ')

for word in words:
    if ord('a') <= ord(word) <= ord('z'):
        print("NO")
        break
else:
    print("YES")