

# 阶乘1
def foo1(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result

print(foo1(-1))
print(foo1(0))
print(foo1(1))
print(foo1(2))
print(foo1(3))


# 阶乘2
# 使用递归，递归就是一个函数调用自身
def foo2(n):
    if n > 1:
        return n * foo2(n - 1)
    else:
        return n

print(foo2(-1))
print(foo2(0))
print(foo2(1))
print(foo2(2))
print(foo2(3))

