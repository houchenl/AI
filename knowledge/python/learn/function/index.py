

# 在函数定义之前调用函数，找不到函数，会报错。说明python是从上到小执行
# 所以文件中函数定义要在函数调用之前
# print(add(1, 2))


# 定义函数1: 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
# pass还可以用在其他语句里
def emptyFunction():
    age = 5
    if age > 15:
        pass
    pass


# 定义参数2：无参数
# 函数名包含多个单词时，全部小写，以下划线拼接
def first_function():
    print('Hello, this is my first function')

first_function()


"""
函数的参数
    - 普通参数(位置参数)(必选参数)
    - 默认参数
    - 可变参数(包裹位置)
    - 关键字参数(包裹关键字)
"""


# 定义函数3：普通参数(位置参数)
# 定义函数时参数的位置和调用函数时参数的位置必须一一对应，也就是说普通参数在调用时是必选参数
def add(num1, num2):
    return num1 + num2

print(add(1, 2))


# 定义函数4：默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面，变化小的参数就可以作为默认参数
# 默认参数可以简化函数的调用, 只有与默认参数不符的时才需要提供额外的信息；另外，无论是简单调用还是复杂调用，函数只需要定义一个
# 所有位置参数必须出现在默认参数前，包括函数定义和调用，否则Python的解释器会报错；
# 按习惯写法，默认参数等号左右两边没有空格
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数，当不按顺序提供部分默认参数时，需要把参数名写上
# 默认参数有个大坑, 含默认参数的函数被调用多次后，如果默认参数被改变，后续默认参数的默认值就是改变后的值，不是最初定义的值，所以默认参数
# 需要为不可变值，如None，String, 数字等
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(power(5))       # 25
print(power(5, 2))    # 25
print(power(5, 3))    # 125
print(power(5, n=4))  # 625


# 定义函数5：可变参数
# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 这些参数在函数调用时自动组装成tuple，然后传入函数
# 可变参数函数调用时，也可以把现成的list或tuple变量名前加*转换成可变参数传进函数。list转换成可变参数时，就自动转换成了tuple
def sum_of_square(*args):
    sum = 0
    for num in args:
        sum += num * num
    return sum

print(sum_of_square(1, 2, 3))    # 14
print(sum_of_square())           # 0
nums1 = [1, 2, 3]
print(sum_of_square(*nums1))     # 14
nums2 = (1, 2, 3)
print(sum_of_square(*nums2))     # 14


# 定义函数6：关键字参数
# 关键字参数可以扩展函数的功能，在必填参数外，使用关键词参数提供可选参数，使函数应对不同情况
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
# 带参数名参数定义和调用时，等号左右不要有空格
# 函数调用输入关键字参数时，可以用0到多个含参数名的参数，也可以传入事先组装好的dict，在dict变量名前加**
def f3(**kw):
    if 'name' in kw:
        print('%s!' % kw['name'])
    elif 'tel' in kw:
        print('%s!' % kw['tel'])
    else:
        print('!')

param = {'name': 'houchen', 'age': 38}
f3(**param)
f3(name='houchen', age=38, tel='13866778899')
f3(user='houchen', age=38, tel='13866778899')
f3(user='houchen', age=38, mobile='13866778899')


# 定义函数7：混合参数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数可以一起使用，或者只用其中某些，但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。最神奇的是通过一个tuple和dict，你也可以调用该函数，
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
def f4(name, age, sex=1, *args, **kw):
    print('name=', name, 'age=', age, 'sex=', sex, 'args=', args, 'kw=', kw)

f4('houchen', 11)
f4('houchen', 22, sex=2)
f4('houchen', 33, 3, 'a', 'b')
f4('houchen', 44, 4, 'a', 'b', x=99)
args = ('houchen', 55, 5, 'a', 'b')
kw = {'x': 99}
f4(*args, **kw)


# 定义函数8：返回多个值
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
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
    return a, b, c        # (11, 22, 33)

print(get_multiple_values())


# 经典函数1：将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

print(factorial(7) // factorial(3) // factorial(4))  # 35, // 是整数除


# 经典函数2：求两个数的最大公约数
# 首先把两个数从小到大排列，然后对小数x从x到1倒序遍历，如果遍历得到数字能被两个数整除，就是公约数，第1个这样的数字就是最大公约数
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

print(gcd(6, 9))


# 经典函数3：求两个数的最小公倍数
# 两个数的乘积 = 最大公约数 * 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(6, 9))


# 辅助函数1：过滤列表时使用
def myfilter(mystr):
    return len(mystr) == 6


'''
内置函数：
    - 数学相关: abs / divmod / pow / round / min / max / sum
    - 序列相关: len / range / next / filter / map / sorted / slice / reversed
    - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
    - 数据结构: dict / list / set / tuple
    - 其他函数: all / any / id / input / open / print / type
'''


print(abs(-1.2345))              # 取绝对值
print(pow(1.2345, 5))            # pow(x, y)，取x的y次方
print(round(-1.5345))            # 返回浮点数x的四舍五入值，没有第2个参数，表示结果取整数
print(round(-1.5345, 3))         # 返回浮点数x的四舍五入值，第2个参数表示结果取n位小数。如果第2个参数为0，结果为xxx.0
fruits = ['orange', 'peach', 'durian', 'watermelon']
my_slice = slice(1, 3)           # slice结果为slice(1, 3, None)，可以传递给list作为参数。 slice(start, stop[, step])
print(fruits[my_slice])          # ['peach', 'durian']，结果列表中包含start，不包含stop，截取列表长度为stop - start
filter_result = filter(myfilter, fruits)
print(filter_result)             # <filter object at 0x1030a14e0>，filter的结果是一个对象，需要转换成list
fruits2 = list(filter_result)    # 将过滤结果转换成列表
print(fruits2)                   # ['orange', 'durian']
print(chr(0x3d))                 # 返回值为=。chr(n)返回(0, 255)数字n对应的ascii码字符，超出这个范围会报错
print(hex(ord('尘')))            # 0x5c18。ord(c)返回对应字符的 ASCII 数值，或者 Unicode 数值，是10进制整数


'''
Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，前三者我们在上面的代码中已经看到了，
所谓的“内置作用域”就是Python内置的那些隐含标识符min、len等都属于内置作用域
在实际开发中，我们应该尽量减少对全局变量的使用，因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，除此之外全局变量
比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被垃圾回收。事实上，减少对全局变量的使用，也是降低代码之间耦合度的一个
重要举措，同时也是对迪米特法则的践行。减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，但是如果我们希望将一个局部变量的
生命周期延长，使其在函数调用结束后依然可以访问，这时候就需要使用闭包，装饰和匿名函数是不同的概念
'''


# 作用域1：局部作用域
def foo1():
    a = 5    # 局部变量

foo1()
# print(a)    # NameError: name 'a' is not defined


# 作用域2：全局作用域
b = 10    # 全局变量

def foo2():
    print(b)

foo2()


# 作用域3：局部变量与全局变量重名时，以局部变量为准
def foo3():
    b = 100    # 局部变量
    print(b)

foo3()


# 作用域4：函数中修改全局变量时，需要声明
# 我们可以使用global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于
# 全局作用域。同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域。
def foo4():
    global b
    b = 200
    print(b)

foo4()
print(b)


# 作用域5：main中的变量是全局变量
def foo5():
    print(c)    # __name__中定义的变量是全局变量

if __name__ == '__main__':
    c = 300    # 全局变量
    foo5()


# 作用域6：嵌套作用域
# 函数内部可以定义函数，内部函数可以访问外部函数中定义的局部变量，外部函数不能调用内部函数的局部变量
def foo6():
    a = 400
    def bar():
        b = 500
        print(a)
        # a = 500    # 在内部函数中定义与外部函数同名的局部变量，变量就会变成内部函数的局部变量，会报错
    print(a)
    bar()

foo6()
# bar()    # 内部函数的作用域在外部函数内部，不能在外部函数外调用


# 作用域7：新的书写方法
# 了解了作用域之后，以后的代码需要以下面的方式书写
def main():
    print('main fucntion')
    # Todo: Add your code here
    pass

if __name__ == '__main__':
    main()

