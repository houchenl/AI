# -*- coding:utf-8 -*-

# python支持的运算符
# +     加
# -     减
# *     乘
# /     除
# //    取整除
# %     取余
# **    幂

a = 9
b = 2
c = a / b   # 4(python2), 4.5(python3)
d = a // b  # 4
e = a % b   # 1
f = a ** b  # 81

print('c is ', c)
print('d is ', d)
print('e is ', e)
print('f is ', f)

b = 2.0
c = a / b   # 4.5
d = a // b  # 4.0
e = a % b   # 1.0
f = a ** b  # 81.0

print('c is ', c)
print('d is ', d)
print('e is ', e)
print('f is ', f)

# 字符串乘
str = 'H' * 10
print(str)      # HHHHHHHHHH



# a += b != a = a + b
a = 10
b = [20]

def test(num, array):
    num += num
    print(num, id(num))    # 20 4305329120，  不可修改变量，新建空间存储结果，新建变量指向新空间
    array += array
    print(array, id(array))    # [20, 20] 4345972552， 可修改变量，在原变量空间对原变量修改

test(a, b)

print(a, id(a))    # 10 4305328800
print(b, id(b))    # [20, 20] 4345972552

# python变量指向的是引用，函数调用时传递的是引用。
# +=操作符对引用指向的数据进行操作，如果是可变类型，直接在数据上进行操作
# 如果是不可变类型，重新开辟空间存储得到的值，并新建一个变量指定新空间。原空间值和原变量指向不变

a = 10
b = [20]

def test2(num, array):
    num = num + num
    print(num, id(num))    # 20 4305329120
    array = array + array
    print(array, id(array))    # [20, 20] 4345972552

test2(a, b)

print(a, id(a))    # 10 4305328800
print(b, id(b))    # [20] 4345971144

# a = a + b，=右边的结果会存在一个新空间，=左边的a为新建变量，指向新空间



