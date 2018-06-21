# -*- coding:utf-8 -*-

# 1. Python内置类型
# 2. 有序集合
# 3. 不能修改，只能查询，不能增删改

# 定义普通元组(tuple)
t = ('Adam', 'Lisa', 'Bart')
print(t)

# 0个元素
t = ()

# 1个元素。()既可以表示tuple类型，也可以列表运算优先级，所以单元素的tuple需要加一个逗号，以免歧义
t = ('Adam', )
print(t)      # ('Adam',)

# tuple和list一样，可以使用索引访问，也支持倒序索引，但不能赋值
print(t[0])   # Adam

# 假如tuple中有n个元素，可以用n个变量，以逗号分隔，来分别取出tuple中对应位置的值
rank = ('A', 'B', 'C')
a, b, c = rank
print('%s, %s, %s' % (a, b, c))

# tuple定义后，就不能改变。没有append方法，也没有insert方法和pop方法。不能添加，不能删除，不能修改

# tuple的元素不可修改，但如果tuple的元素本身可以修改，如是一个list，那tuple的内容可以间接通过子内容修改
z = (1, True, ['a', 'b'])
print(z)    # (1, True, ['a', 'b'])
z[2][0] = 'x'
z[2][1] = 'y'
print(z)    # (1, True, ['x', 'y'])
