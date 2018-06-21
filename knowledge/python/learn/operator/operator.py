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

