# N = int(input())
# tree = {}
#
# for _ in range(N):
#     root, left, right = input().split()
#     tree[root] = [left, right]
#
#
# def start(root):
#     if root != '.':
#         print(root, end='')
#         start(tree[root][0])
#         start(tree[root][1])
#
# def mid(root):
#     if root != '.':
#         mid(tree[root][0])
#         print(root, end='')
#         mid(tree[root][1])
#
# def end(root):
#     if root != '.':
#         end(tree[root][0])
#         end(tree[root][1])
#         print(root, end='')
#
# start('A')
# print()
# mid('A')
# print()
# end('A')

print(10000000000 % 12)