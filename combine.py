import numpy

def combine(array1, array2):
    assert array1.shape == array2.shape,      'Arrays must have the same shape'
    assert isinstance(array1, numpy.ndarray), 'Input must be numpy arrays'
    assert isinstance(array2, numpy.ndarray), 'Input must be numpy arrays'

    flatarr = numpy.array([], dtype=numpy.int16)
    indlist = []    
    for nd, val1 in numpy.ndenumerate(array1):
        val2 = array2[nd[0],nd[1]]
        if (val1,val2) not in indlist:
            indlist.append((val1,val2))
        ind = indlist.index((val1,val2))
        flatarr = numpy.append(flatarr, ind)
    outarr = flatarr.reshape(array2.shape)
    return outarr


# TEST
a1 = numpy.array([[ 0, 0, 0, 1],\
                  [ 0, 0, 0, 1],\
                  [ 0, 0, 0, 1],\
                  [ 1, 1, 1, 1]])

a2 = numpy.array([[ 2, 2, 3, 3],\
                  [ 2, 2, 3, 3],\
                  [ 3, 3, 3, 3],\
                  [ 3, 3, 3, 3]])

output = combine(a1,a2)
print output


'''
([[0, 0, 1, 2],
  [0, 0, 1, 2],
  [1, 1, 1, 2],
  [2, 2, 2, 2]])
'''
