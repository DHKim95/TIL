kill, death, assist = map(int, input().split('/'))

if kill + assist < death or death == 0:
    print("hasu")
else:
    print("gosu")