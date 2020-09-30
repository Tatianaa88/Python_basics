def func_div(a, b):
    if b == 0:
        return 0
    else:
        result = a/b
        return result


user_num1 = int(input('Please enter number 1: '))
user_num2 = int(input('Please enter number 2: '))

div_result = func_div(user_num1, user_num2)
if div_result == 0:
    print('Division by 0 is not allowed.')
else:
    print(div_result)
