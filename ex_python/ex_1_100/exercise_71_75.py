
#example 71

'''
N = 3
#stu
#num: string
#name: string
#score[4]: list

student = []
for i in range(5):
	student.append(['','',[]])

def input_stu(stu):
	for i in range(N):
		stu[i][0] = raw_input('input student num:\n')
		stu[i][1] = raw_input('input student name:\n')
		for j in range(3):
			stu[i][2].append(int(raw_input('score:\n')))

def output_stu(stu):
	for i in range(N):
		print '%-6s%-10s' %(stu[i][0],stu[i][1])
		for j in range(3):
			print '%-8d' %stu[i][2][j]

if __name__ == '__main__':
	input_stu(student)
	print student
	output_stu(student)			


'''

#example 72
'''
#create a list

if __name__ == '__main__':
	ptr = []
	for i in range(5):
		num = int(raw_input('please input a number:\n'))	
		ptr.append(num)
	print ptr
'''

#example 73
'''
if __name__ == '__main__':
	ptr = []
	for i in range(5):
		num = int(raw_input('please input a number:\n'))
		ptr.append(num)
	print ptr
	ptr.reverse()
	print 'reverse after'
	print ptr

'''


#example 74
'''
if __name__ == '__main__':
	arr1 = [3,12,8,9,11]
	print 'original sequence'
	ptr = list(arr1)
	print ptr
	print 'sort after'
	ptr.sort()
	print ptr

'''

#example 75


if __name__ == '__main__':
	for i in range(5):
		n = 0
		if i !=1:
			n += 1
		if i == 3:
			n += 1
		if i == 4:
			n += 1
		if i != 4:
			n += 1
		if n == 3:
			print 64+i