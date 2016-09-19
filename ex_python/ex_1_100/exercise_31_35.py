#!/usr/bin/python

#example 31
'''
letter = raw_input('please input:')
#while letter != 'Y'
if letter == 'S':
	print('please input second letter:')
	letter = raw_input('please input:')
	if letter == 'a':
		print ('saturday')
	elif letter == 'u':
		print ('Sunday')
	else:
		print ('date error.')
elif letter == 'F':
	print ('Friday')
elif letter == 'M':
	print ('Monday')
elif letter == 'T':
	print ('please input second letter')
	letter = raw_input('please input:')
	if letter == 'u':
		print('Tuesday')
	elif letter == 'h':
		print('Thursday')
	else:
		print('data error')
elif letter == 'W':
	print('Wednesday')
else:
	print('data error')
'''

#example 32
'''
a = ['one','two','three']
for i in a[::-1]:
	print i

'''

#example 33

#way one
'''
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1
'''
#way two
'''
L = [1,2,3,4,5]
temp = ','
s1 = ''
for i in range(5):
	if(i < 4):
		s1 += str(L[i])+temp
	else:
		s1 += str(L[i])
print s1
'''


#example 34

#origin code
'''
def hello_world():
	print 'hello world'

def three_hellos():
	for i in range(3):
		hello_world()

if __name__ == '__main__':
	three_hellos()
'''

#test call function
'''
def test():
	for i in range(4):
		print i*2

def test_two():
	for i in range(4):
		test()
		print

if __name__ == '__main__':
	test_two()

'''

#example 35

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FALL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
print bcolors.WARNING + 'warning color font?' + bcolors.ENDC

