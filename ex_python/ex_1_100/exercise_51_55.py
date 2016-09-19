#!/usr/bin/python

#example 51
'''
if __name__ == '__main__':
	a = 077
	b = a &3
	print ' a& b = %d' %b
	b &= 7
	print 'a & b = %d' %b
'''


#example 52
'''
if __name__ == '__main__':
	a = 077 
	b = a | 3
	print ' a | b is %d' %b
	b |= 7
	print 'a | b is %d' %b
'''


#example 53
'''
if __name__ == '__main__':
	a = 077
	b = a^3
	print 'the  a^3 = %d' %b
	b ^= 7
	print 'the a ^b = %d' %b
'''

#example 54
'''
if __name__ == '__main__':
	a = int(raw_input('input number\n'))
	b = a >> 4
	c = ~(~0 << 4)
	d = b & c
	print '%o\t%o' %(a,b)


'''

#example 55

if __name__ == '__main__':
	a = 234
	b = ~a
	print 'the a\'s 1 complement is %d' %b
	a = ~a
	print 'the a\'s 2 complement is %d' %a