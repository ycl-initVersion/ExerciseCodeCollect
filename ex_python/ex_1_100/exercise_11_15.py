#!/usr/bin/python

#print 'hello world'


#sample 11
'''
f1 = 1
f2 = 1
for i in range(1,21):
	print '%12d %12d' % (f1,f2)
	if(i % 2 == 0):
		print ''
	f1 = f1 + f2
	f2 = f1 + f2

'''


#sample 12
'''
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,200):
	k = int(sqrt(m+1))
	for i in range(2,k+1):
		if m % i == 0:
			leap = 0
			break
	if leap == 1:
		print '%-4d' % m
        h += 1
        if h % 10 == 0:
        	print ''
	leap = 1
print 'the total is %d' % h    
'''

#sample 13
'''
for n in range(100,1000):
	i = n /100
	j = n/10%10
	k = n%10
	if n == i ** 3 + j ** 3 + k ** 3:
		print n
'''

#sample 14
'''
from sys import stdout
n = int(raw_input("input number:\n"))
print 'n = %d' % n

for i in range(2,n+1):
	while n != i:
		if n % i == 0:
			stdout.write(str(i))
			stdout.write("*")
			n = n / i
		else:
			break
print '%d' % n	

'''

#example 15

score = int(raw_input("input score\n"))
if score >= 90:
	grade = 'A'
elif score >= 60:
	grade = 'B'
else:
	grade = 'C'
print '%d beglongs to %s' % (score,grade)						