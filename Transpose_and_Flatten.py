import numpy

n, m = map(int, input().split())

lest = [input().split() for i in range(n)]

result = numpy.array(lest , numpy.int)
print(result.transpose())
print(result.flatten())
