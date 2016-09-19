
#example 81
'''
a = 809
for i in range(10,100):
	b = i* a + 1
	if b >= 1000 and b <= 10000 and 8*i < 100 and 9 *i >= 100:
		print b,'/',i,' = 809 * ',i,' + ',b%i

'''

#example 82
'''
if __name__ == '__main__':
	n = 0
	p = raw_input('input a octal number:\n')
	for i in range(len(p)):
		n = n * 8 + ord(p[i]) - ord('0')
	print n

'''

#example 83
'''
if __name__ == '__main__':
	sum = 4
	s = 4
	for j in range(2,9):
		print sum
		if j <= 2:
			s *= 7
		else:
			s *= 8
		sum += s
	print 'sum = %d' %sum
'''


#example 84
'''
delimiter = ','
mylist = ['brazil','russia','india','china']
print delimiter.join(mylist)


'''


#example 85

if __name__ == '__main__':
	zi = int(raw_input('input a number:\n'))
	n1 = 1
	c9 = 1
	m9 = 9
	sum = 9
	while  n1 != 0:
		if sum % zi == 0:
			n1 = 0
		else:
			m9 += 10
			sum += m9
			c9 += 1
	print '%d can be divided by %d 9' %(sum,c9)

