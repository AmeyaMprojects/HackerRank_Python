import numpy

def arrays(arr):
    arr.reverse()
    result = numpy.array(list(map(float,arr)))
  ## in a single line we have mapped the list to a float and then created a array using numpy
    return result
        

arr = input().strip().split(' ')
