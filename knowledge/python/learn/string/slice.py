name = 'abcdefABCDEF'

str = name[2:5]
print(str)    # cde

str = name[2:-1]
print(str)

str = name[2:]
print(str)
str = name[:2]
print(str)
str = name[:]
print(str)

str = name[2:-1:2]   # start : end : step
print(str)
str = name[-1:0:-1]
str = name[-1::-1]
