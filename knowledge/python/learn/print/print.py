# -*- coding:utf-8 -*-

# 打印字符串，逗号会被显示为空格
# 上下两句打印效果相同
print("hello", "world")
print("hello world")

# 打印运算结果 100 + 200 = 300
# 逗号会被打印成1个空格
print('100 + 200 =', (100 + 200))

age = 18
print('age is %d' % age)

name = "后尘"
print('name is %s' % name)

weight = 55.3
print('weight is %f' % weight)
# %f打印输出默认是6位小数，如果想显示x位小数，需要设置为%.xf
print('weight is %.2f' % weight)

# print多个值
print('name is %s, age is %d, weight is %.1f' % (name, age, weight))

# 其它格式化符号
# %c    字符
# %s    字符串
# %i    有符号十进制整数
# %d    有符号十进制整数
# %u    无符号十进制整数
# %o    八进制整数
# %x    十六进制整数（小写字母）
# %X    十六进制整数（大写字母）
# %e    科学计数法，索引符号使用小写e
# %E    科学计数法，索引符号使用大写E
# %f    浮点实数
# %g    %f和%e的简写
# %G    %f和%E的简写

