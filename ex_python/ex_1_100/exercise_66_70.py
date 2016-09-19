
#example 66

'''

if __name__ == '__main__':
	n1 = int(raw_input('n1 = :\n'))
	n2 = int(raw_input('n2 = :\n'))
	n3 = int(raw_input('n3 = :\n'))

	def swap(p1,p2):
		return p2,p1

	if n1 > n2:
		n1,n2 = swap(n1,n2)
	if n1 > n3:
		n1,n3 = swap(n1,n3)
	if n2 > n3:
		n2,n3 = swap(n2,n3)


	print n1,n2,n3

'''


#example 67

'''
def inp(numbers):
	for i in range(9):
		numbers.append(int(raw_input('input a number:\n')))
	numbers.append(int(raw_input('input a number:\n')))

p = 0
def max_min(array):
	max = min = 0
	for i in range(1,len(array)-1):
		p = i
		if array[p] > array[max]:
			max = p
		elif array[p] < array[min]:
			min = p
	k = max
	l = min
	array[0],array[l] = array[l],array[0]
	array[9],array[k] = array[k],array[9]

def outp(numbers):
	for i in range(len(numbers)):
		print numbers[i]


if __name__ == '__main__':
	array = []
	inp(array)
	max_min(array)
	outp(array)
'''


#example 68

'''
if __name__ == '__main__':
	n = int(raw_input('the total number is :\n'))
	m = int(raw_input('back m:\n'))

	def move(array,n,m):
		array_end = array[n-1]
		for i in range(n-1,-1,-1):
			array[i] = array[i-1]
		array[0] = array_end
		m -= 1
		if m > 0:
			move(array,n,m)

	number = []
	for i in range(n):
		number.append(int(raw_input('input a number:\n')))
	print 'original number:', number

	move(number,n,m)

	print 'after number:', number

'''

#example 69

'''
if __name__ == '__main__':
	nmax = 50
	n = int(raw_input('please input total numbers:\n'))
	num = []
	for i in range(n):
		num.append(i+1)

	i = 0
	k = 0
	m = 0

	while m<n-1:
		if num[i] != 0 :
			k += 1
		if k == 3:
			num[i] = 0
			k = 0
			m += 1
		i += 1
		if i ==n:
			i = 0
	i = 0
	while num[i] ==0:
		i += 1
	print num[i]

'''

#example 70

if __name__ == '__main__':
	s = raw_input('please input a string:\n')
	print 'the string has %d characters.' %len(s)