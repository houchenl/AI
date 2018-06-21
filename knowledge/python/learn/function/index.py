
# 定义函数1: 无参数
# def functionName():
#    pass
# 函数名包含多个单词时，全部小写，以下划线拼接
def first_function():
    print('Hello, this is my first function')

# 在函数定义之前调用函数，找不到函数，会报错。说明python是从上到小执行
# 所以文件中有多个函数定义时，把所有函数的定义统一放在函数调用的上方
# print(add(1, 2))

# 定义函数2：带参数
def add(num1, num2):
    return num1 + num2

# 定义函数3：返回多个值
def get_multiple_values():
    a = 11
    b = 22
    c = 33

    # 第1种：用一个列表封装多个值，返回列表，实现多个值一起返回
    # d = [a, b, c]
    # return d     # [11, 22, 33]

    # 第2种：用一个元组封装多个值，返回元组
    # d = (a, b, c)
    # return d     # (11, 22, 33)

    # 第3种：直接组装返回列表
    # return [a, b, c]      # [11, 22, 33]

    # 第4种：直接组装返回元组
    # return (a, b, c)      # (11, 22, 33)

    # 第5种，直接返回多个变量，中间以逗号分隔。python会自动把它们打包成元组，然后返回
    # return a, b, c        # (11, 22, 33)

# 函数调用：functionName(param1, param2, ...)
first_function()
print(add(1, 2))
print(get_multiple_values())
