# 定义函数: 实现加减乘除的计算器
# 分别使用函数定义:加法/减法/乘法/除法的算法
# 在计算器函数中分别去调用对应的函数,返回计算的结果

def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1, number2):
    return number1 * number2

def div(number1, number2):
    if number2 != 0:
        return number1 / number2
    raise Exception('分母不能为0')

def calculator(f, number1, number2):
    if f == add:
        return add(number1, number2)
    elif f == mul:
        return mul(number1, number2)
    elif f == sub:
        return sub(number1, number2)
    elif f == div:
        return div(number1, number2)
    else:
        print('只能计算加减乘除')

print(calculator(add, 13, 4))
print(calculator(div, 13, 10))