from itertools import permutations, combinations

array = [1,2,3,4]

# 순열
per_lst = list(permutations(array,2))
print(per_lst)

# 조합
com_lst = list(combinations(array,2))
print(com_lst)