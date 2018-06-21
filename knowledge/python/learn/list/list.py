
bicycles = ['trek', 'cannondale', 'redline']
# print(bicycles)
# print(bicycles[0])
# print(bicycles[-1])
# print(bicycles[1:3])

# append (tail)
bicycles.append('ducati')
# print(bicycles)

# insert (position)
bicycles.insert(1, 'phoenix')
# print(bicycles)

# extend
names = ['one', 'two', 'three']
result = bicycles + names
print(result)

bicycles.extend(names)
print(bicycles)

nums = [1, 2, 3]
# print(nums)

bicycles.insert(2, nums)
# print(bicycles)       # ['trek', 'phoenix', [1, 2, 3], 'cannondale', 'redline', 'ducati']
# print(bicycles[2])    # [1, 2, 3]

# del (position)
del bicycles[2]
# print(bicycles)

# pop (tail or position)
bike = bicycles.pop()
# print(bicycles)
# print(bike)

bike = bicycles.pop(0)
# print(bicycles)

# remove (value), remove first match value
bicycles.remove('redline')
# print(bicycles)


cars = ['bmw', 'audi', 'toyota', 'subaru']

# sort list for ever
# cars.sort()    # ['audi', 'bmw', 'subaru', 'toyota']
# print(cars)
# cars.sort(reverse=True)    # ['toyota', 'subaru', 'bmw', 'audi']
# print(cars)

# sort list one time for use
# print(sorted(cars))    # ['audi', 'bmw', 'subaru', 'toyota']
# print(sorted(cars, reverse=True))    # ['toyota', 'subaru', 'bmw', 'audi']

print(cars)
cars.reverse()
print(cars)

length = len(cars)
print(length)

# in, not in

