#!/usr/bin/python

'''

# exercise_006.py

#way one

def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a


print fib(10)

'''

# way two
# use di gui
'''
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)

print fib(10)

'''

def fib(n):
	if n == 1:
		return [1]
	if n == 2:
		return  [1,1]
	fibs = [1,1]
	for i in range(2,n):
		fibs.append(fibs[-1]+fib[-2])
    return fibs

#input the top 10 number
print fib(10)


