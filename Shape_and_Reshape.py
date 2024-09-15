##https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
import numpy
inp = (input().strip().split(" "))
## taking input and converting to a list using .split()
int_inp = (map(int,inp))
## mapping the list to integer type 
result = numpy.array(list(int_inp))
## converting the list to an array
print (numpy.reshape(result,(3,3)))
## reshaping the array to a 3x3 array and printing
