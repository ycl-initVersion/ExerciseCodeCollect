#!usr/bin/python

#example 46
'''
TRUE = 1
FALSE = 0
def SQ(x):
	return x*x
print 'if the imput number is less than 50, the progress will abort'
again = 1
while  again:
	num = int(raw_input('please input number'))
	print 'the result is %d' %(SQ(num))
	if num >= 50:
		again = TRUE
	else:
		again = FALSE
'''


#example 47
'''
def exchange(a,b):
	a,b = b,a
	return (a,b)

if __name__ == '__main__':
	x = 10
	y = 20
	print 'x = %d ,y = %d' %(x,y)
	x,y = exchange(x,y)
	print 'x = %d, y = %d' %(x,y)		

'''

#example 48
'''
if __name__ == '__main__':
	i = 10
	j = 20
	if i > j:
		print '%d large than %d' %(i,j)
	elif i == j:
		print '%d is equal %d' %(i,j)
	elif i < j:
		print '%d is less than %d' %(i,j)
	else:
		print "don't know"
'''


#example 49
'''
MAXIMUN = lambda x,y:(x>y)*x + (x<y)*y
MINIMUN = lambda x,y:(x>y)*y + (x<y)*x

if __name__ == '__main__':
	a = 10
	b = 20
	print 'the larger one is %d' %MAXIMUN(a,b)
	print 'the lower one is %d' %MINIMUN(a,b)

'''

#example 50


import random

print random.uniform(10,20)
