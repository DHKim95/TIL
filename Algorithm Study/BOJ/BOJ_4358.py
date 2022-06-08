import sys

tree_lst = {}
cnt = 0

while True:
    name = sys.stdin.readline().strip()
    if not name:
        break

    # 사전에 없는것을 추가해준다.
    tree_lst.setdefault(name, 0)
    tree_lst[name] += 1 # 갯수 추가
    cnt += 1

for name in sorted(tree_lst.keys()):
    print('{} {:.4f}'.format(name, tree_lst[name] * 100 / cnt))