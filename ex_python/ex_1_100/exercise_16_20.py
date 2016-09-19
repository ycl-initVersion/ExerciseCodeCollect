

#example 16
'''
import datetime

if __name__ == '__main__':
	print(datetime.date.today().strftime('%d/%m/%Y'))

	miyazakiBirthDate = datetime.date(1941,1,5)
	print(miyazakiBirthDate.strftime('%d/%m/%Y'))
	miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
	print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
	miyazakiFirstBirthDate = miyazakiBirthDate.replace(year=miyazakiBirthDate.year+1)
	print(miyazakiFirstBirthDate.strftime('%d/%m/%Y'))
'''


#example 17
'''
import string
s = raw_input('input a string:\n')
letters = 0
space = 0 
digit = 0
others = 0
for c in s:
	if c.isalpha():
		letters += 1
	elif c.isspace():
		space += 1
	elif c.isdigit():
		digit += 1
	else:
		others += 1

print 'char = %d,space = %d,digit = %d,others = %d' %(letters,space,digit,others)
'''

#exaple 18
'''
Tn = 0
Sn = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a= :\n'))
for count in range(n):
	Tn = Tn + a
	a = a * 10
	Sn.append(Tn)
	print Tn

Sn = reduce(lambda x,y:x + y,Sn)
print Sn
'''

#example 19
'''
from sys import stdout
for j in range(2,1001):
	k = []
	n = -1
	s = j
	for i in range(1,j):
		if j % i == 0:
			n += 1
			s -= i
			k.append(i)
	if s == 0:
		print j
		for i in range(n):
			stdout.write(str(k[i]))
			stdout.write(' ')
		print k[n]
'''


#example 20

Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
	Sn += 2*Hn
	Hn /=2

print 'total of road is %f' %Sn
print 'the tenth of %f meter' %Hn