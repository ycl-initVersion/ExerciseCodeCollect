#!/usr/bin/python

#example 21
'''
x2 = 1
for day in range(9,0,-1):
	x1 = (x2+1) * 2
	x2 = x1

print x1
'''


#example 22
'''
for i in range(ord('x'),ord('z')+1):
	for j in range(ord('x'),ord('z')+1):
		if i!=j:
			for k in range(ord('x'),ord('z')+1):
				if (i != k) and (j != k):
					if(i != ord('x')) and ( k != ord('x')) and (k != ord('z')):
						print 'order is a --%s\t b-- %s\t c--%s\t' %(chr(i),chr(j),chr(k))
'''

#example 23
'''
from sys import stdout
for i in range(4):
	for j in range(2-i+1):
		stdout.write(' ')
	for k in range(2*i + 1):
		stdout.write('*')
	print

for i in range(3):
	for j in range(i+1):
		stdout.write(' ')
	for k in range(4-2*i + 1):
		stdout.write('*')
	print
'''

#example 24

#way one
'''
a = 2.0
b = 1.0
s = 0
for n in range(1,21):
	s += a/b
	t = a
	a = a+b
	b = t
print s
'''


#way two
'''
a= 2.0
b = 1.0
s = 0.0
for n in range(1,21):
	s += a/b
	b,a = a,a+b
print s
'''

#way three
'''
a = 2.0
b = 1.0
l = []
for n in range(1,21):
	b,a = a,a+b
	l.append(a/b)
print reduce(lambda x,y:x+y,l)
'''

#example 25

#way one
'''
n = 0
s = 0
t = 1
for n in range(1,21):
	t *= n
	s += t
print '1!+2!+...+20! = %d' %s 

'''

#way two
s = 0
l = range(1,21)
def op(x):
	r = 1
	for i in range(1,x+1):
		r *= i
	return r
s = sum(map(op,l))
print '1!+2!+...+20!=%d' %s 