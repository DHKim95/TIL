array = [2,4,3,5,1,6]
target = 3

# 재귀
def binary_search(array, target, left, right):
    middle = (left+right)//2
    mid = array[middle]
    if target == mid:
        print("answer {}".format(target))
    elif mid > target:
        binary_search(array, target, left, middle-1)
    elif mid < target:
        binary_search(array, target, middle+1, right)
    else:
        return False

# 반복문
while left <= right:
    mid = (left+right)//2
    if array[mid] == target:
        print(target)
        break
    elif array[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
