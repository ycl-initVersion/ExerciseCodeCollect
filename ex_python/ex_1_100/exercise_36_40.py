#!/usr/bin/python
# -*- coding: UTF-8 -*-

#example 36


'''
from math import sqrt
if __name__ == '__main__':
    N = 100
    a = range(0,N)
    for i in range(2,int(sqrt(N))):
        for j in range(i + 1,N):
            if (a[i] != 0) and (a[j] != 0):
                if a[j] % a[i] == 0:
                    a[j] = 0
    print
    for i in range(2,N):
        if a[i] != 0:
            print "%5d" % a[i]
            if (i - 2) % 10 == 0:
                print

'''

#example 37

'''
if __name__ == "__main__":
    N = 10
    # input data
    print 'please input ten num:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('input a number:\n')))
    print
    for i in range(N):
        print l[i]
    print

    # sort ten num
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print 'after sorted'
    for i in range(N):
        print l[i]            
'''

#example 38

'''
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum
'''


#example 39

'''
if __name__ == '__main__':
    # 方法一
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print 'original list is:'
    for i in range(len(a)):
        print a[i]
    number = int(raw_input("insert a new number:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    for i in range(11):
        print a[i]

'''


#example 40


if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a) 
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print a      

      