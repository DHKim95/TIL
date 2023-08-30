from collections import defaultdict

dic = defaultdict(int)
total_cnt = 0

while True:
    words = input()
    if not words:
        break

    dic[words] += 1
    total_cnt += 1

tree_name = sorted(list(dic.keys()))
print(tree_name)
for name in tree_name:
    print("{} {:.4f}".format(name, (dic[name]/total_cnt) * 100))
