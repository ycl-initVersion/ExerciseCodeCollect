#!usr/bin/python


#example 41
'''
def varfun():
	var = 0
	print 'var = %d' %var
	var += 1

if __name__ == '__main__':
	for i in range(3):
		varfun()


#the attribute of class
class Static:
	StaticVar = 5
	def varfunc(self):
		self.StaticVar += 1
		print self.StaticVar

print Static.StaticVar
a = Static()
print 
for i in range(3):
	a.varfunc()
print

b = Static()
for i in range(3):
	b.varfunc()
'''


#example 42
'''
num = 2
def autofunc():
	num = 1
	print 'internal block num = %d' %num
	num += 1
for i in range(3):
	print 'the num = %d' %num
	num += 1
	autofunc()

'''


#example 43

'''
class Num:
	nNum = 1
	def inc(self):
		self.nNum += 1
		print 'nNum = %d' %self.nNum

if __name__ == "__main__":
	nNum = 2
	inst = Num()
	for i in range(3):
		nNum += 1 
		print 'the num = %d' %nNum
		inst.inc()
'''

#example 44
'''
import external

if __name__ == "__main__":
	print external.add(10,20)		
'''

#example 45

tmp =0 
for i in range(1,101):
	tmp += i
print 'the sum is  %d' %tmp