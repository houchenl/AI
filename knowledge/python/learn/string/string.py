# 打印双引号
print('Learn "Python" in imooc.')

# 打印单引号
print("I'm Chinese.")

# 既打印单引号，也打印双引号，使用转义
print('Bob said \"I\'m Ok\".')
print("Bob said \"I\'m Ok\".")
print('Bob said "I\'m Ok".')
print("Bob said \"I'm Ok\".")
#print(r'Bob said "I'm Ok".')   not ok

# r字符串中的特殊字符(不包含单/双引号)不做转义
str1 = r'\(~_~)/\(~_~)/'
print(str1)

# 多行字符串
str1 = '''第一行
第二行
第三行'''
print(str1)

str1 = '第一行\n第二行\n第三行'
print(str1)

# 多行文本中的引号不用转义
str1 = '''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print(str1)

# 中文
str1 = '云横秦岭家何在，雪拥蓝关马不前。'    # OK
str2 = u'云横秦岭家何在，雪拥蓝关马不前。'    # OK
print(str1)
print(str2)

# 通过索引获取字符串中字符
str1 = 'Hello everyone.'
print(str1[0])
print(str1[-1])    # 最后一个字符是-1，而不是-0

# 通过:截取字符串中的值
print(str1[0:4])
print(str1[:4])    # 等价于 [0:4]
print(str1[:-1])   # 前n-1个字符
print(str1[:])     # 所有字符
print(str1[-4:])   # -4到最后

# 字符串连接 +
str1 = 'Hello'
str2 = 'World'
str3 = str1 + str2
print(str3)

# 字符串连接 ,
#str3 = str1, str2    ('Hello', 'World')
print(str1, str2)     # 'Hello World'

# 重复字符串 *
str2 = str1 * 3
print(str2)

# 判断字符串是否包含某些字符串
str1 = 'Hello World'
str2 = 'llo'
flag = str2 in str1
flag2 = str2 not in str1
print(flag)
print(flag2)

# 把字符串