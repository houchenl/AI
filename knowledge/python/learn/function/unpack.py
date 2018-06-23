
# 测试拆包*
A = (1, 2, 3)
print(A)     # (1, 2, 3)
print(*A)    # 1, 2, 3

# 测试拆包**
B = {'name': 'houchenl', 'age': 28}
print(B)     # {'name': 'houchenl', 'age': 28}
# print(**B) # 打印会出错

# 总结
# * 可以对list和tuple进行拆包，拆包结果可以打印，也可以作为参数传递给*args
# ** 可以对字典进行拆包，拆包结果不可以打印，可以作为参数传递给**args
