### 整数
print(12 + 0x12)

### 浮点数
print(1234.5)
print(1.2345e3)

### 字符串
print("Where there is a will, there is a way.")
print('where there is a will, there is a way.')

### 布尔值
# Python把0、空字符串''和None看成False
# 其它数值和非空字符串看成True
print(True)
print(False)
# and运算时，如果第一个参数是True，运算结果是第二个参数
# 如果第一个参数是False，运算结果就是False
print(True and 8)    # 8
print(False and 8)    # False
# 非0数值，包括字符串，被视为True，所以取
print(8 and 3)    # 3
print(-8.2 and -9)    # -9
# 0被视为False，所以取第1个参数的值作为运算结果
print(0 and True)    # 0
print(0 and False)    # 0

### 空值
print(None)
