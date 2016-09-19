
#!/usr/bin/python

#coding=utf-8

#example 26
'''
def fact(j):
	sum = 0
	if j == 0:
		sum = 1;
	else:
		sum = j * fact(j-1)
	return sum

for i in range(5):
	print '%d! = %d' %(i,fact(i))

'''

#example 27
'''
def output(s,l):
	if l == 0:
		return
	print (s[l-1])
	output(s,l-1)

s = raw_input('input a string:')
l = len(s)
output(s,l)
'''

#example 28
'''

def age(n):
	if n == 1:
		c = 10
	else:
		c = age(n-1)+2
	return c

print age(5)
'''


#example 29
'''
x = int(raw_input('please enter a number:\n'))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x %10

if a != 0:
	print 'five bite number:',e,d,c,b,a
elif b != 0:
	print 'four bite number:',e,d,c,b
elif c != 0:
	print 'three bite number:',e,d,c 
elif d != 0:
	print 'two bite number:',e,d
else:
	print 'one bite number:', e
'''

#example 30
a = int(raw_input('please enter a number:\n'))
x = str(a)
flag = True

for i in range(len(x)/2):
	if x[i] != x[-i-1]:
		flag = False
		break
if flag:
	print '%d is a hui wen shu' % a
else:
	print '%d is not a hui wen shu' %a

