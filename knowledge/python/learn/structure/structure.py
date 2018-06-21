# if
age = 20
if age > 18:
    print('adult')

# if .. else ..
age = 16
if age > 18:
    print('adult')
else:
    print('teenager')

# if .. elif .. else ..
age = 10
if age >= 18:
    print('adult')
elif age > 10:
    print('teenager')
elif age > 3:
    print('kid')
else:
    print('baby')

# for
names = ['Adam', 'Lisa', 'Bart']
for name in names:
    print(name)

# while
i = 0
count = 5
while i < count:
    print(i)
    i = i + 1

# break
i = 0
while True:
	print(i)
	i = i + 1
	if i == 5:
		break

# continue
scores = (75, 98, 59, 81, 66, 43, 69, 85)
sum = 0
num = 0
for score in scores:
	if score < 60:
		continue
	sum = sum + score
	num = num + 1
print(sum / num)
