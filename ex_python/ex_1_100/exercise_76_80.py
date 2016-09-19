
#example 76
'''
def peven(n):
	i = 0
	s = 0.0
	for i in range(2,n+1,2):
		s += 1.0/i
	return s

def podd(n):
	s = 0.0
	for i in range(1,n+1,2):
		s += 1/i
	return s

def dcall(fp,n):
	s = fp(n)
	return s


if __name__ == '__main__':
	n = int(raw_input('input a number:\n'))
	if n%2 == 0:
		sum = dcall(peven,n)
	else:
		sum  = dcall(podd,n)
	print sum
'''


#example 77
'''
if __name__ == '__main__':
	s = ["man","woman","girl","boy","sister"]
	for i in range(len(s)):
		print s[i]
'''


#example 78
'''
if __name__ == '__main__':
	person = ["li":0,"wang":50,"zhang":20,"sun":22]
	m = 'li'
	for key in person.keys():
		if person[m] < person[key]:
			m = key
	print '%s,%d' %(m,person[m])
'''

#example 79
'''
if __name__ == '__main__':
	str1 = raw_input('input string:\n')
	str2 = raw_input('input string:\n')
	str3 = raw_input('input string :\n')
	print str1,str2,str3

	if str1> str2:
		str1,str2 = str2,str1
	if str1 > str3:
		str1,str3 = str3,str1
	if str2>str3:
		str2,str3 = str3,str2

	print 'after being sorted'
	print str1,str2,str3

'''

#example 80

if __name__ == "__main__":
	i = 0
	j = 1
	x = 0
	while (i<5):
		x = 4*j
		for i in range(0,5):
			if (x%4 != 0):
				break
			else:
				i += 1
			x = (x/4)*5+ 1
		j += 1
	print x