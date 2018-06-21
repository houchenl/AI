
str = 'hello world, my name is houchen'

# find
result = str.find('world')
print(result)    # start index of world in str. -1 means has no match string

# rfind
# find match string from right to left

# index
# if find match string, return start index
# if find no match string, exception

# rindex
# from right to left

# count
result = str.count('world')
print(result)

# replace
# replace all match
result = str.replace('world', 'WORLD')
print(result)
# replace match xxx times
result = str.replace('world', 'WORLD', 1)

# split
# get an array
result = str.split(' ')
# if no keyword, all \t space \n will be removed

# title
# every word's first letter captain

# capitalize
# string's first word's first letter captain

# startswith
# result is boolean

# endswith
# result is boolean

# lower
# all letters in string lower

# upper
# string's all letters upper

lyric = '想要陪你看大海'
# ljust
print(lyric.ljust(50))

# rjust
print(lyric.rjust(50))

# center
print(lyric.center(50))

# lstrip
# remove blank charactors in left, \n \t blank

# rstrip
# remove blank charactors in right, \n \t blank

# strip
# remove blank charactors in left and right, \n \t blank

# partition
# return a tuple, split string into three groups, key word in middle

# rpartition
# from right to left find match place

# splitlines
# split string into array by \n

# isalpha
# whether all letters in string are alpha

# isdigit
# all letters are all number

# isalnum
# all letters are alpha or number

# isspace
# are all letters in string are space

# join
# join array's string into one string by key word
a = ['111', '222', '333']
b = ','
c = b.join(a)

test = 'adkfjq  ie\nofj al\n\ndf jkqo \t\n ie\tfja  ldskfj  qweifj\t  als\tdfjq  iwe ofj'
result = test.split()
print(result)
