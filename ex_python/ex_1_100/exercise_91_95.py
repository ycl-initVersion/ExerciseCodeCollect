
#example 91
'''
#use time function

if __name__ == '__main__':
	import time
	print time.ctime(time.time())
	print time.asctime(time.localtime(time.time()))
	print time.asctime(time.gmtime(time.time()))
'''

#example 92
'''
if __name__ == '__main__':
	import time
	start = time.time()
	for i in range(3000):
		print i
	end = time.time()

	print end - start
'''

#example 93

'''
if __name__ == '__main__':
	import time
	start = time.clock()
	for i in range(10000):
		print i
	end = time.clock()
	print 'different is 6.3%f' %(end - start)
'''

#example 94
'''
if __name__ == '__main__':
	 import time
	 import random

	 play_it = raw_input('do you want to play it.(\'y\' or \'n\')')
	 while play_it == 'y':
	 	c = raw_input('input a character:\n')
	 	i = random.randint(0,2**32)%100
	 	print 'please input number you guess:\n'
	 	start = time.clock()
	 	a  = time.time()
	 	guess = int(raw_input('input your guess:\n'))
	 	while guess != i:
	 		if guess > i:
	 			print 'please input a little smaller'
	 			guess = int(raw_input('input you guess:\n'))
	 		else:
	 			print 'please input a little bigger'
	 			guess = int(raw_input('input your guess:\n'))
	 	end = time.clock()
	 	b = time.time()
	 	var = (end - start) / 18.2
	 	print var
	 	#print 'it took you %6.3 seconds' %time.difftime(b,a)
	 	if var < 15:
	 		print 'you are very clever'
	 	elif var < 25:
	 		print 'you are normal'
	 	else:
	 		print 'you are stupid'
	 	print 'congradulations'
	 	print 'the number you guess is %d ' %i
	 	play_it = raw_input('do you want to play it')

'''

#example 95
'''
from dateutil import parser
dt = parser.parse('Aug 28 2015 12:00AM')
print dt
'''