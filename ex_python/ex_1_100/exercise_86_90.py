
#example 86
'''
if __name__ == '__main__':
	a = 'acdstewrt'
	b = 'basdfsdf'
	c = a +'-'+ b
	print c 
'''


#example 87

'''
#use struct pass varibale


if __name__ == '__main__':
	class student:
		x = 0
		c = 0
	def f(stu):
		stu.x = 20
		stu.c = 'c'

	a = student()
	a.x = 3
	a.c = 'a'
	f(a)
	print a.x,a.c

'''

#example 88
'''
if __name__ == '__main__':
	n = 1
	while n <= 7:
		a = int(raw_input('input a number:\n'))
		while a < 1 or a > 50:
			a = int(raw_input('input a number:\n'))
		print a * '*'
		n += 1
'''

#test * operator

'''
a = 8
print a * 'c'
'''


#exmaple 89
'''
if __name__ == '__main__':
	ptr = []
	for i in range(5):
		num = int(raw_input('please input a number:\n'))
		ptr.append(num)
	print ptr
'''

#sample two
'''
from sys import stdout
if __name__ == '__main__':
	a = int(raw_input('input a number:\n'))
	aa = []
	aa.append(a%10)
	aa.append(a % 100 /10)
	aa.append(a%1000 /100)
	aa.append(a / 1000)

	for i in range(4):
		aa[i] += 5
		aa[i] %= 10
	for i in range(2):
		aa[i],aa[3-i] = aa[3-i],aa[i]
	for i in range(3,-1,-1):
		stdout.write(str(aa[i]))

'''


#example 90

#test the usage of the lig

testList = [10086,'chinese mobile',[1,2,3,4,5]]

print len(testList)

print testList[1:]

testList.append('i\'m new here!')

print len(testList)
print testList[-1]

print testList.pop(1)
print len(testList)
print testList

matrix = [[1,2,3],
[4,5,6],
[7,8,9]]

print matrix
print matrix[1]
col2 = [row[1] for row in matrix]
print col2
col2even = [row[1] for row in matrix if row[1] %2 == 0]
print col2even
