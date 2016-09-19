
#example 61

'''
#print yang hui san jiao

if __name__ == '__main__':
	a = []
	for i in range(10):
		a.append([])
		for j in range(10):
			a[i].append(0)
	for i in range(10):
		a[i][0] = 1
		a[i][i] = 1
	for i in range(2,10):
		for j in range(1,i):
			a[i][j] = a[i-1][j-1] + a[i-1][j]
	from sys import stdout
	for i in range(10):
		for j in range(i+1):
			stdout.write(str(a[i][j]))
			stdout.write(' ')
		print
'''


#example 62
'''
#find string

str1 = 'abcdefg'
str2 = 'cde'
print str1.find(str2)

'''

#example 63

'''
#drar ellipse.

if __name__ == '__main__':
	from Tkinter import *
	x = 360
	y = 160
	top = y - 30
	bottom = y - 30

	canvas = Canvas(width = 400,height = 600, bg = 'white')
	for i in range(20):
		canvas.create_oval(250-top,250-bottom,250+top,250+bottom)
		top -= 5
		bottom += 5
	canvas.pack()
	mainloop()

'''


#example 64

#draw ellipse and rectangle
'''
if __name__ == '__main__':
	from Tkinter import *
	canvas = Canvas(width = 400,height = 600,bg = 'white')
	left = 20
	right = 50
	top = 50
	num = 15
	for i in range(num):
		canvas.create_oval(250-right,250-left,250+right,250+left)
		canvas.create_oval(250-20,250-top,250+20,250+top)
		canvas.create_rectangle(20-2*i,20-2*i,10*(i+2),10*(i+2))
		right += 5
		left += 5
		top += 10

	canvas.pack()
	mainloop()
'''


#example 65

#draw a graphic

import math
class PTS:
	def __init__(self):
		self.x = 0
		self.y = 0

points = []

def LineToDemo():
	from Tkinter import *
	screenx = 400
	screeny = 400
	canvas = Canvas(width = screenx,height = screeny,bg = 'white')

	AspectRatio = 0.85
	MAXPTS = 15
	h = screeny
	w = screenx
	xcenter = w / 2
	ycenter = h / 2
	radius = (h - 30)/(AspectRatio*2)-20
	step = 360/MAXPTS
	angle = 0.0
	for i in range(MAXPTS):
		rads = angle * math.pi / 180.0
		p = PTS()
		p.x = xcenter + int(math.cos(rads)*radius)
		p.y = ycenter - int(math.sin(rads)*radius*AspectRatio)
		angle += step
		points.append(p)
	canvas.create_oval(xcenter - radius,ycenter - radius,
		xcenter + radius,ycenter + radius)

	for i in range(MAXPTS):
		for j in range(i,MAXPTS):
			canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)

	canvas.pack()
	mainloop()

if __name__ == '__main__':
	LineToDemo()		