import numpy
import itertools

def combine(array1, array2):
    assert array1.shape == array2.shape,      'Arrays must have the same shape'
    assert isinstance(array1, numpy.ndarray), 'Input must be numpy arrays'
    assert isinstance(array2, numpy.ndarray), 'Input must be numpy arrays'

    q1 = list(numpy.unique(array1))
    q2 = list(numpy.unique(array2))
    comb = list(itertools.product(q1,q2))

    keys = {}
    flatarr = numpy.array([], dtype=numpy.int16)
    for nd, val1 in numpy.ndenumerate(array1):
        val2 = array2[nd[0],nd[1]]
        ind = comb.index((val1, val2))
        flatarr = numpy.append(flatarr, ind)
        if not keys.has_key(ind):
            keys[ind]=(val1,val2)

    rank = {e:n for n,e in enumerate(numpy.unique(flatarr))}
    out1 = numpy.array([], dtype=numpy.int16)
    for x in flatarr:
        out1 = numpy.append(out1, rank[x])    
    outarr = out1.reshape(array2.shape)
    return outarr, keys


# TEST
a1 = numpy.array([[ 0, 0, 0, 1],
                  [ 0, 0, 0, 1],
                  [ 0, 0, 0, 1],
                  [ 1, 1, 1, 1]])

a2 = numpy.array([[ 2, 2, 3, 3],
                  [ 2, 2, 3, 3],
                  [ 3, 3, 3, 3],
                  [ 3, 3, 3, 3]])

output, k = combine(a1,a2)
print output
print k

'''
([[0, 0, 1, 2],
 [0, 0, 1, 2],
 [1, 1, 1, 2],
 [2, 2, 2, 2]])
{0: (0, 2), 1: (0, 3), 3: (1, 3)}
'''
