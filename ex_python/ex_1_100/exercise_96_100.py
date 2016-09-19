
#example 96
'''
if __name__ == '__main__':
	str1 = raw_input('input a string:\n')
	str2 = raw_input('input a sub string:\n')
	ncount = str1.count(str2)
	print ncount

'''


#example 97

'''
#test write string to file

if __name__ == '__main__':
	from sys import stdout
	filename = raw_input('input a file name:\n')
	fp = open(filename,"w")
	ch = raw_input('input string:\n')
	while ch != '#':
		fp.write(ch)
		stdout.write(ch)
		ch = raw_input('')
	fp.close()
'''


#example 98

'''
if __name__ == '__main__':
	fp = open('test.txt','w')
	str = raw_input('please input a string:\n')
	str = str.upper()
	fp.write(str)
	fp = open('test.txt','r')
	print fp.read()
	fp.close()
'''

#example 99
'''
if __name__ == '__main__':
	import string
	fp = open('test1.txt')
	a = fp.read()
	fp.close()

	fp = open('test2.txt')
	b = fp.read()
	fp.close()

	fp = open('test3.txt','w')
	l = list(a+b)
	l.sort()
	s = ''
	s = s.join(l)
	print s
	fp.write(s)
	fp.close()
'''


#example 100

i = ['a','b']
l = [1,2]
print dict([i,l])