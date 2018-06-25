
# 函数式编程
# 1. 函数式编程允许把函数作为参数传入另一个函数，还允许返回另一个参数
# 2. 纯粹的函数式编程语言没有变量，相同输入有相同输出，这种纯函数称为没有副作用
# 3. python对函数式编程部分支持。因为python允许使用变量，所以不是纯函数式编程语言


# 高阶函数 (Higher-order function)

# 1. 函数可以赋值给变量，可以通过变量来调用函数
f = abs
print(f(-10))    # 10

# 2. 函数名其实就是指向函数的变量，把函数名赋值后，就不能再用函数名调用函数
# abs = 10
# print(abs(-10))    # Error: 'int' object is not callable

# 3. 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    print(x, y, f)    # -5 6 <built-in function abs>
    return f(x) + f(y)

print(add(-5, 6, abs))    # 11

# 4. map/reduce
# map函数接收两个参数，第一个是函数，第二个是Interable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def square(x):
    return x * x

result = map(square, [1, 2, 3, 4, 5, 6, 7, 8, 9])    # python3 map返回的结果是迭代器
print(list(result))    # 输出迭代器需要转化为列表, list(iterator), [1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce函数也接收两个参数，第一个函数，第二个iterable。函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

def f10(x, y):
    return x * 10 + y

result = reduce(f10, [1, 2, 3, 4, 5, 6, 7, 8, 9])    # 123456789

# string to int by map/reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(f10, map(char2num, s))

result = str2int('678912345')    # 678912345

# 5. filter
# filter接收两个参数，第一个是函数，第二个是序列
# filter把函数依次作用于每个元素，根据返回值是True还是False决定保留还是丢弃。返回值是iterator
# 对一个列表，删除偶数，保留奇数
def is_odd(n):
    return n % 2 == 1

result = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])    # <filter object at 0x1040a1320>
print(list(result))    # [1, 3, 5, 7, 9]

# 6. sorted
# python内置的sorted函数可以对列表进行排序。对数字默认从小到大排序
print(sorted([36, 5, -12, 9, -21]))    # [-21, -12, 5, 9, 36]
# sorted是高阶函数，可以接收一个key函数实现自定义排序，如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))    # [5, 9, -12, -21, 36]
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
# 如果要求忽略大小写，就先把字符串变成大写或小写，如下，其中str是一个类
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))    # ['about', 'bob', 'Credit', 'Zoo']
# 如果要反向排序，传第三个参数，reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))    # ['Zoo', 'Credit', 'bob', 'about']

