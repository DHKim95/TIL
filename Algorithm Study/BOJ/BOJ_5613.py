number = int(input())

while True:
    operation = input()
    if operation == '=':
        break
    N = int(input())
    if operation == '+':
        number += N
    elif operation == '-':
        number -= N
    elif operation == '*':
        number *= N
    elif operation == '/':
        number //= N
print(number)